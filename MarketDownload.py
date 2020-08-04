from tkinter import *
from tkinter import IntVar
import sqlite3
import requests
import json
import datetime


def close(n):
    if n == 2:
        MarketOutput.destroy()
    if n == 1:
        MarketFrame.destroy()


def LoadMarketInitiation():
    # RIGHT FRAME with Editor widgets to be positioned under

    global MarketFrame
    MarketFrame = Tk()
    MarketFrame.geometry("300x200")
    MarketFrame.config(background='#FAEBD7')

    LatestDateFrame = LabelFrame(MarketFrame, text='Market Download', padx=0, pady=0, bg='#FAEBD7')
    LatestDateFrame.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

    global DownloadRequestFrame
    DownloadRequestFrame = LabelFrame(MarketFrame, text="Download Request", padx=0, pady=0, bg='#CDB79E')
    DownloadRequestFrame.grid(row=1, column=0, padx=5, pady=5)

    # LOGIC DETERMINING LATEST AVAILABLE MARKET SNAPSHOT
    Submission = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id={}'
                              '&api_key=d925d4e1950ddf067dd0daff2b0d399d&file_type=json'.format('ICERATES1100USD30Y'))
    Submission_output = json.loads(Submission.content)

    dateRange = []
    for i in range(len(Submission_output['observations'])):
        dateRange.append(Submission_output['observations'][i]['date'])
    LatestMarket = (max(dateRange))

    # Declaration of latest market availability:
    defaultLabel = Label(LatestDateFrame, text="Latest Market Available: " + str(LatestMarket), font=10, bg='#FAEBD7',
                         anchor=N)
    defaultLabel.grid(row=0, column=0, columnspan=2)

    def marketDownload(number):

        conn = sqlite3.connect('financial_Calculator.db', timeout=1)
        c = conn.cursor()

        try:
            c.execute("""
        CREATE TABLE MarketRates (
            rate_type text,
            rate_name text,
            seriesID text,
            rate integer,
            date text
            )""")
        except:
            print('table already exists')
        conn.commit()
        conn.close()

        # List of LiborSwap series_ID:
        LiborSwapIDList = [
            ['USDONTD156N', 'O/N Libor'],
            ['USD1WKD156N', '1WK Libor'],
            ['USD1MTD156N', '1M Libor'],
            ['USD2MTD156N', '2M Libor'],
            ['USD3MTD156N', '3M Libor'],
            ['USD6MTD156N', '6M Libor'],
            ['USD12MD156N', '12M Libor'],
            ['ICERATES1100USD1Y', '1Yr Swap'],
            ['ICERATES1100USD2Y', '2Yr Swap'],
            ['ICERATES1100USD3Y', '3Yr Swap'],
            ['ICERATES1100USD4Y', '4Yr Swap'],
            ['ICERATES1100USD5Y', '5Yr Swap'],
            ['ICERATES1100USD6Y', '6Yr Swap'],
            ['ICERATES1100USD7Y', '7Yr Swap'],
            ['ICERATES1100USD8Y', '8Yr Swap'],
            ['ICERATES1100USD9Y', '9Yr Swap'],
            ['ICERATES1100USD10Y', '10Yr Swap'],
            ['ICERATES1100USD15Y', '15Yr Swap'],
            ['ICERATES1100USD20Y', '20Yr Swap'],
            ['ICERATES1100USD30Y', '30Yr Swap']
        ]

        # List for Treasury series IDs
        TreasuryIDList = [
            ['DGS1MO', '1M Treasury'],
            ['DGS3MO', '3M Treasury'],
            ['DGS6MO', '6M Treasury'],
            ['DGS1', '1Y Treasury'],
            ['DGS2', '2Y Treasury'],
            ['DGS3', '3Y Treasury'],
            ['DGS5', '5Y Treasury'],
            ['DGS7', '7Y Treasury'],
            ['DGS10', '10Y Treasury'],
            ['DGS20', '20Y Treasury'],
            ['DGS30', '30Y Treasury']
        ]
        securitylist = []
        if number == 1:
            securitylist = LiborSwapIDList
            security = 'LiborSwap'
        if number == 2:
            securitylist = TreasuryIDList
            security = 'Treasury'

        # List for exporting out the rates and loading into SQLite3
        ratesoutputlist = []

        conn = sqlite3.connect('financial_Calculator.db')
        c = conn.cursor()

        # Elimination of duplicate downloads:

        c.execute(
            "DELETE FROM MarketRates WHERE date = " + "'" + LatestMarket + "'" + " and rate_type = " + "'" + security + "'")
        conn.commit()

        for seriesID in securitylist:
            # Connection to
            Submission = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id={}'
                                      '&api_key=d925d4e1950ddf067dd0daff2b0d399d&file_type=json'.format(seriesID[0]))
            Submission_output = json.loads(Submission.content)

            interestRate = (Submission_output['observations'][int(len(Submission_output['observations']) - 1)]['value'])

            c.execute("INSERT INTO MarketRates VALUES (:rt,:rn,:sid,:r,:d)",
                      {
                          'rt': security,
                          'rn': seriesID[1],
                          'sid': seriesID[0],
                          'r': interestRate,
                          'd': LatestMarket,

                      })

            # Commit changes
            conn.commit()

        c.execute("SELECT * FROM MarketRates WHERE date = " + "'" + LatestMarket + "'")
        retrieve = c.fetchall()

        OutputText = '{:^30}{:^30}{:^30}{:^30}\n'.format('Rate Identifier', 'Tenor', 'Rate', 'Date')
        OutputText = OutputText + '{:=<30}{:=<30}{:=<30}{:=<30}\n'.format('=', '=', '=', '=')

        for i in retrieve:
            OutputText = OutputText + '{:^30}{:^30}{:^30}{:^30}\n'.format(i[0], i[1][0:3], str(round(i[3], 2)), i[4])
        conn.close()

        global MarketOutput

        MarketOutput = Tk()
        MarketOutput.config(background='Black')
        CloseButton = Button(MarketOutput, text='CLOSE', command=lambda: close(2), highlightbackground='Black').pack()
        timeStamp = Label(MarketOutput, text="Program executed: " + str(datetime.datetime.now())[
                                                                    0:19] + "  |   Sourced: Federal Reserve Economic Data (FRED) API",
                          background='black', fg='green').pack()
        OutputLabel = Label(MarketOutput, text=OutputText, bg='Black', fg='green').pack()

        MarketOutput.mainloop()

    # Download Requests:
    LiborLabel = Label(DownloadRequestFrame, text="Libor-Swap: ", bg='#CDB79E')
    LiborLabel.grid(row=0, column=0)

    LiborButton = Button(DownloadRequestFrame, text="Download ", highlightbackground='#CDB79E',
                         command=lambda: marketDownload(1))
    LiborButton.grid(row=0, column=1)

    LiborLabel = Label(DownloadRequestFrame, text="Treasury: ", bg='#CDB79E')
    LiborLabel.grid(row=1, column=0)

    LiborButton = Button(DownloadRequestFrame, text="Download ", highlightbackground='#CDB79E',
                         command=lambda: marketDownload(2))
    LiborButton.grid(row=1, column=1)

    closeButton = Button(MarketFrame, text='CLOSE', command=lambda: close(1), highlightbackground='#FAEBD7')
    closeButton.grid(row=4, column=0, columnspan=3)

    MarketFrame.mainloop()
