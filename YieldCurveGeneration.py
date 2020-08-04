from tkinter import *
from tkinter import IntVar
import sqlite3
import requests
import json
import datetime
import matplotlib as plt
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


def YieldCurveGeneration():
    # Establishment of mainframe
    YCGen = Tk()
    YCGen.geometry("300x300")
    YCGen.configure(background='#FAEBD7')

    # Defining market selection date
    def MarketSelection():
        global marketdate
        marketdate = vardate.get()
        print(marketdate)

    # Defining Instrument selection
    def InstrumentSelection():
        global InstrumentType
        InstrumentType = varinstrument.get()
        print(InstrumentType)

    # Defining Interpolation selection date:
    def IntMarketSelection():
        global intmarketdate
        intmarketdate = vardate.get()
        print(intmarketdate)

    # Defining Interpolation selection instrument:
    def intinstrumentselection():
        global intinstrument
        intinstrument = Intvarinstrument.get()
        print(intinstrument)

    # Running Interpolation Logic
    def Interpolation():
        conn = sqlite3.connect('financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT * from MarketRates WHERE date = " + "'" + marketdate + "'" + " and rate_type = " + "'" + InstrumentType + "'")
        retrieval = c.fetchall()

        if InstrumentType == 'Treasury':
            TreasuryTenor = [1, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]

            TenorList = []
            i = 0;
            for record in retrieval:
                TenorList.append([record[0], TreasuryTenor[i], record[3]])
                i = i + 1

            # Generation of interpolations:
            interpolationlist = [];
            for i in TenorList:
                if i[1] == 1:
                    previousPosition = i
                    interpolationlist.append(previousPosition)
                if i[1] != 1:
                    newPosition = i
                    interpolationCount = newPosition[1] - previousPosition[1] - 1
                    incrementalIncrease = (newPosition[2] - previousPosition[2]) / (interpolationCount + 1)

                    for n in range(interpolationCount):
                        newTenor = previousPosition[1] + (n + 1)
                        newRate = previousPosition[2] + (n + 1) * incrementalIncrease
                        interpolationlist.append(["Treasury", newTenor, newRate])
                    interpolationlist.append(["Treasury", newPosition[1], newPosition[2]])
                    previousPosition = newPosition

        if InstrumentType == 'LiborSwap':
            TreasuryTenor = [1, 2, 3, 6, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 180, 240, 360]

            TenorList = []
            i = 0;
            for record in retrieval:
                if record[1] not in ['O/N Libor', '1WK Libor', '12M Libor']:
                    TenorList.append([record[0], TreasuryTenor[i], record[3]])
                    i = i + 1

            # Generation of interpolations:
            interpolationlist = [];
            for i in TenorList:
                if i[1] == 1:
                    previousPosition = i
                    interpolationlist.append(previousPosition)
                if i[1] != 1:
                    newPosition = i
                    interpolationCount = newPosition[1] - previousPosition[1] - 1
                    incrementalIncrease = (newPosition[2] - previousPosition[2]) / (interpolationCount + 1)

                    for n in range(interpolationCount):
                        newTenor = previousPosition[1] + (n + 1)
                        newRate = previousPosition[2] + (n + 1) * incrementalIncrease
                        interpolationlist.append(["LiborSwap", newTenor, newRate])
                    interpolationlist.append(["LiborSwap", newPosition[1], newPosition[2]])
                    previousPosition = newPosition

        # Update Interpolation into SQL RECORDS
        # (1)    CREATE TABLE IF NOT IN EXISTANCE

        try:
            c.execute("""
        CREATE TABLE InterpolationRates (
            rate_type text,
            rate_tenor integer,
            rate integer,
            date text
            )""")
        except:
            print('table already exists')
        conn.commit()

        # (2)    Clear DUPLICATE RECORDS
        c.execute(
            "DELETE FROM InterpolationRates WHERE date = " + "'" + vardate.get() + "'" + " and rate_type = " + "'" + InstrumentType + "'")
        conn.commit()

        # (3)    INSERT INTO ABOVE TABLE THE VALUE OF THE RECORDS
        for record in interpolationlist:
            c.execute("INSERT INTO InterpolationRates VALUES (:rt,:t,:r,:d)",
                      {
                          'rt': InstrumentType,
                          't': record[1],
                          'r': record[2],
                          'd': vardate.get()
                      })

        # Commit changes
        conn.commit()

        c.execute("SELECT * FROM InterpolationRates")
        global InterpolationRetrieval
        InterpolationRetrieval = c.fetchall()
        for i in retrieval:
            print(i)

        conn.close()

    # Retrieval of Interpolation SQL Data and Graphing of the output
    def GraphInt():
        print(intinstrument + " " + intmarketdate + " ")

        # Extraction of data from SQL
        conn = sqlite3.connect('financial_Calculator.db')
        c = conn.cursor()

        # Retrieve uniquely available dates:

        c.execute("SELECT * from InterpolationRates WHERE date ={} and rate_type ={}".
                  format("'" + intmarketdate + "'", "'" + intinstrument + "'"))
        conn.commit()

        retrieval = c.fetchall()

        rates = [];
        tenor = []
        for record in retrieval:
            tenor.append(record[1]);
            rates.append(record[2])

        # Graphing assembly:

        plt.pyplot.plot(tenor, rates)
        plt.pyplot.xlabel('Tenor')
        plt.pyplot.ylabel('Rates')
        plt.pyplot.show()

    def bootStrap():
        #Retrieve available interpolation rates:
        conn = sqlite3.connect('financial_Calculator.db')
        c = conn.cursor()
        c.execute("SELECT * from InterpolationRates WHERE date ='2020-07-02' and rate_type = 'Treasury' and rate_tenor < 360")
        conn.commit()

        retrieval = c.fetchall()

        #Initiation for bootstrapping
        bootstrap = [];

        n=1
        for record in retrieval:
            print(record[2])
            discount = 0; discountvector = 1
            if record[1]==1:
                bootstrap.append([record[0],record[1],record[2],record[3]])
            else:
                for i in bootstrap:

                    discount = (record[2]/1200)/((1+i[2]/100)**(i[1]/12))
                    discountvector -= discount

                x=(1+record[2]/1200)/discountvector
                shortrate = ((x**(12/record[1])) - 1)*100
                bootstrap.append([record[0],record[1],shortrate,record[3]])
            n+=1
        for i in bootstrap:
            print(i)
    # Establishing Market Date Selection Option
    vardate = StringVar()
    vardate.set("Choose a day")

    varinstrument = StringVar()
    varinstrument.set("Select Instrument")

    conn = sqlite3.connect('financial_Calculator.db')
    c = conn.cursor()

    # Retrieve uniquely available dates:

    c.execute("SELECT DISTINCT date from MarketRates")
    conn.commit()

    DateOptions = [];
    InstrumentOptions = []

    retrieval = c.fetchall()
    for dates in retrieval:
        DateOptions.append(dates[0])

    c.execute("SELECT DISTINCT rate_type from MarketRates")

    retrieval = c.fetchall()
    for instrument in retrieval:
        InstrumentOptions.append(instrument[0])

    conn.close()

    # YC Generation Widgets:
    DateLabel = Label(YCGen, text="Select Market date\n for Bootstrapping", bg='#FAEBD7').grid(row=0, column=0)
    drop = OptionMenu(YCGen, vardate, *DateOptions)
    drop.grid(row=0, column=1)
    drop.config(bg='#FAEBD7')

    selectMarket = Button(YCGen, text="Enter", command=MarketSelection)
    selectMarket.grid(row=0, column=2)
    selectMarket.config(highlightbackground='#FAEBD7')

    YCLabel = Label(YCGen, text="Select Instrument type\n for Bootstrapping", bg='#FAEBD7').grid(row=1, column=0)

    drop2 = OptionMenu(YCGen, varinstrument, *InstrumentOptions)
    drop2.grid(row=1, column=1)
    drop2.config(bg='#FAEBD7')

    selectInstrument = Button(YCGen, text="Enter", command=InstrumentSelection)
    selectInstrument.grid(row=1, column=2)
    selectInstrument.config(highlightbackground='#FAEBD7')

    Interpolation = Button(YCGen, text="Interpolate", command=Interpolation, highlightbackground="#FAEBD7").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10)
    Bootstrap = Button(YCGen, text = "Bootstrap", command=bootStrap,highlightbackground = "#FAEBD7").grid(row=2,column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10)


    # Interpolation Result Output

    # Establishing Market Date Selection Option
    Intvardate = StringVar()
    Intvardate.set("Choose a day")

    Intvarinstrument = StringVar()
    Intvarinstrument.set("Select Instrument")

    conn = sqlite3.connect('financial_Calculator.db')
    c = conn.cursor()

    # Retrieve uniquely available dates:

    c.execute("SELECT DISTINCT date from InterpolationRates")
    conn.commit()

    IntDateOptions = [];
    IntInstrumentOptions = []

    retrieval = c.fetchall()
    for dates in retrieval:
        IntDateOptions.append(dates[0])

    c.execute("SELECT DISTINCT rate_type from InterpolationRates")

    retrieval = c.fetchall()
    for instrument in retrieval:
        IntInstrumentOptions.append(instrument[0])

    conn.close()

    InterpolationOutputFrame = LabelFrame(YCGen, bg='#CDB79E', text='Interpolation Graphical Output')
    InterpolationOutputFrame.grid(columnspan=3, row=3, column=0, padx=10, pady=10)
    DateLabel = Label(InterpolationOutputFrame, text="Select Market date", bg='#CDB79E').grid(row=0, column=0)

    drop = OptionMenu(InterpolationOutputFrame, vardate, *IntDateOptions)
    drop.grid(row=0, column=1)
    drop.config(bg='#CDB79E')

    selectMarket = Button(InterpolationOutputFrame, text="Enter",
                          command=IntMarketSelection, highlightbackground='#CDB79E').grid(row=0, column=2)

    InstrumentLabel = Label(InterpolationOutputFrame, text="Select Instrument", bg='#CDB79E').grid(row=1, column=0)

    drop2 = OptionMenu(InterpolationOutputFrame, Intvarinstrument, *IntInstrumentOptions)
    drop2.grid(row=1, column=1)
    drop2.config(bg='#CDB79E')

    SelectInstrument = Button(InterpolationOutputFrame, text="Enter",
                              command=intinstrumentselection, highlightbackground='#CDB79E').grid(row=1, column=2)

    GraphInt = Button(InterpolationOutputFrame, text="Interpolate", command=GraphInt,
                      highlightbackground="#CDB79E").grid(row=2, column=0, padx=10, pady=10)
