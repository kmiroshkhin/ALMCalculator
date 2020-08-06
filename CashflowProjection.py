from tkinter import *
from ALMCalculator.Analytics.SQLQuery import *

def StatusBar():
    productList = SQLQuery
    productList = productList.distinctproductassetclass(SQLQuery,dateClick.get())
    print(productList,dateClick.get())

    for product in productList:
        StatusBar = LabelFrame(PositionFrame, text="Status Bar", padx=5, pady=5, bg='#CDB79E',height=300,width=300)
        StatusBar.grid(row=2, column=0, padx=200, pady=10);StatusBar.grid_propagate(0)

        Current_Instrument = Label(StatusBar, text=product, bg='#CDB79E')
        Current_Instrument.grid(row=0, column=0)

def CF_Forecast():
    # Assembly of main frame
    global PositionFrame
    PositionFrame = Tk()
    PositionFrame.geometry("800x400")
    PositionFrame.config(background='#FAEBD7')

    # Assembly of LabelFrame
    global PositionAssembly
    PositionAssembly = LabelFrame(PositionFrame, text="Position Review", padx=5, pady=5, bg='#CDB79E')
    PositionAssembly.grid(row=1, column=0, padx=200, pady=5)

    # Portfolio Selection
    TotalAmount = Label(PositionAssembly, text="Select Portfolio Date: ", bg='#CDB79E')
    TotalAmount.grid(row=0, column=0)

    getdate = SQLQuery()
    getdate = getdate.distinctportfoliodates()

    global dateClick
    dateClick = StringVar()
    PortfolioDrop = OptionMenu(PositionAssembly,dateClick,*getdate)
    PortfolioDrop.grid(row=0,column=1)
    PortfolioDrop.config(highlightbackground='#FAEBD7')

    selectInstrument = Button(PositionAssembly, text="Execute CF Run", command=StatusBar)
    selectInstrument.grid(row=0, column=2,padx=5, pady=5)
    selectInstrument.config(highlightbackground='#FAEBD7')