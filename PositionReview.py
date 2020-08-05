from tkinter import *
from ALMCalculator.Analytics.InstrumentGenerator import *
from ALMCalculator.Analytics.SQLQuery import *

def Report():
    print(dateClick.get())
    ReportAssembly = LabelFrame(PositionFrame,text = "Balance sheet Output", padx=5, pady=5, bg='#CDB79E')
    ReportAssembly.grid(row=2, column=0, padx=5, pady=5)

    TotalAmount = Label(ReportAssembly, text="As-Of-Date:        " + dateClick.get(), bg='#CDB79E')
    TotalAmount.grid(row=0, column=0,columnspan=10)

    #Headers
    Assets = Label(ReportAssembly, text="Assets", bg='#CDB79E')
    Assets.grid(row=1, column=0,columnspan=5)

    Liabilities = Label(ReportAssembly, text="Liabilities", bg='#CDB79E')
    Liabilities.grid(row=1, column=6, columnspan=5)

    #Heasers Assets
    Instrument = Label(ReportAssembly, text="Instrument |", bg='#CDB79E')
    Instrument.grid(row=2, column=0)
    Balance = Label(ReportAssembly, text="Balance MM |", bg='#CDB79E')
    Balance.grid(row=2, column=1)
    Coupon = Label(ReportAssembly, text="Coupon |", bg='#CDB79E')
    Coupon.grid(row=2, column=2)
    Maturity = Label(ReportAssembly, text="Maturity |", bg='#CDB79E')
    Maturity.grid(row=2, column=3)
    Counter = Label(ReportAssembly, text="Position Count", bg='#CDB79E')
    Counter.grid(row=2, column=4)
    blank = Label(ReportAssembly, text="                ", bg='#CDB79E')
    blank.grid(row=2, column=5)


    #Cash
    cashbalance = SQLQuery();cashbalance=cashbalance.getbalance("Cash",dateClick.get(),"Asset")
    cashcoupon = SQLQuery();cashcoupon = cashcoupon.getcoupon("Cash",dateClick.get(),"Asset")
    cashmaturity = SQLQuery();cashmaturity = cashmaturity.getmaturity("Cash",dateClick.get(),"Asset")
    cashcount = SQLQuery();cashcount = cashcount.getquantity("Cash",dateClick.get(),"Asset")

    Instrument = Label(ReportAssembly, text="Cash", bg='#CDB79E')
    Instrument.grid(row=3, column=0)
    Balance = Label(ReportAssembly, text=cashbalance, bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=3, column=1)
    Coupon = Label(ReportAssembly, text=cashcoupon, bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=3, column=2)
    Maturity = Label(ReportAssembly, text=cashmaturity, bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=3, column=3)
    Count = Label(ReportAssembly, text=cashcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=3, column=4)


    #Mortgage
    mortgagebalance = SQLQuery();mortgagebalance=mortgagebalance.getbalance("Mortgage",dateClick.get(),"Asset")
    Mortgagecoupon = SQLQuery();Mortgagecoupon = Mortgagecoupon.getcoupon("Mortgage",dateClick.get(),"Asset")
    Mortgagematurity = SQLQuery();Mortgagematurity = Mortgagematurity.getmaturity("Mortgage",dateClick.get(),"Asset")
    Mortgagecount = SQLQuery();Mortgagecount = Mortgagecount.getquantity("Mortgage",dateClick.get(),"Asset")

    Instrument = Label(ReportAssembly, text="Mortgage", bg='#CDB79E')
    Instrument.grid(row=4, column=0)
    Balance = Label(ReportAssembly, text=mortgagebalance, bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=4, column=1)
    Coupon = Label(ReportAssembly, text=Mortgagecoupon, bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=4, column=2)
    Maturity = Label(ReportAssembly, text=Mortgagematurity, bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=4, column=3)
    Count = Label(ReportAssembly, text=Mortgagecount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=4, column=4)

    #CRE
    CREbalance = SQLQuery();CREbalance=CREbalance.getbalance("CRE",dateClick.get(),"Asset")
    CREcoupon = SQLQuery();CREcoupon = CREcoupon.getcoupon("CRE",dateClick.get(),"Asset")
    CREmaturity = SQLQuery();CREmaturity = CREmaturity.getmaturity("CRE",dateClick.get(),"Asset")
    CREcount = SQLQuery();CREcount = CREcount.getquantity("CRE", dateClick.get(),"Asset")

    Instrument = Label(ReportAssembly, text="CRE", bg='#CDB79E')
    Instrument.grid(row=5, column=0)
    Balance = Label(ReportAssembly, text=CREbalance, bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=5, column=1)
    Coupon = Label(ReportAssembly, text=CREcoupon, bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=5, column=2)
    Maturity = Label(ReportAssembly, text=CREmaturity, bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=5, column=3)
    Count = Label(ReportAssembly, text=CREcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=5, column=4)

    # C&I
    CIbalance = SQLQuery();CIbalance = CIbalance.getbalance("C&I", dateClick.get(),"Asset")
    CIcoupon = SQLQuery();CIcoupon = CIcoupon.getcoupon("C&I", dateClick.get(),"Asset")
    CImaturity = SQLQuery();CImaturity = CImaturity.getmaturity("C&I", dateClick.get(),"Asset")
    CIcount = SQLQuery();CIcount = CIcount.getquantity("C&I", dateClick.get(),"Asset")

    Instrument = Label(ReportAssembly, text="C&I", bg='#CDB79E')
    Instrument.grid(row=6, column=0)
    Balance = Label(ReportAssembly, text=CIbalance, bg='#CDB79E', fg='#0101DF')
    Balance.grid(row=6, column=1)
    Coupon = Label(ReportAssembly, text=CIcoupon, bg='#CDB79E', fg='#0101DF')
    Coupon.grid(row=6, column=2)
    Maturity = Label(ReportAssembly, text=CImaturity, bg='#CDB79E', fg='#0101DF')
    Maturity.grid(row=6, column=3)
    Count = Label(ReportAssembly, text=CIcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=6, column=4)

    # Wholesale
    Wbalance = SQLQuery();Wbalance = Wbalance.getbalance("Wholesale", dateClick.get(),"Asset")
    Wcoupon = SQLQuery();Wcoupon = Wcoupon.getcoupon("Wholesale", dateClick.get(),"Asset")
    Wmaturity = SQLQuery();Wmaturity = Wmaturity.getmaturity("Wholesale", dateClick.get(),"Asset")
    Wcount = SQLQuery();Wcount = Wcount.getquantity("Wholesale", dateClick.get(),"Asset")

    Instrument = Label(ReportAssembly, text="Wholesale", bg='#CDB79E')
    Instrument.grid(row=7, column=0)
    Balance = Label(ReportAssembly, text=Wbalance, bg='#CDB79E', fg='#0101DF')
    Balance.grid(row=7, column=1)
    Coupon = Label(ReportAssembly, text=Wcoupon, bg='#CDB79E', fg='#0101DF')
    Coupon.grid(row=7, column=2)
    Maturity = Label(ReportAssembly, text=Wmaturity, bg='#CDB79E', fg='#0101DF')
    Maturity.grid(row=7, column=3)
    Count = Label(ReportAssembly, text=Wcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=7, column=4)

    #Heasers Liabilities
    Instrument = Label(ReportAssembly, text="       Instrument |", bg='#CDB79E')
    Instrument.grid(row=2, column=5)
    Balance = Label(ReportAssembly, text="Balance MM |", bg='#CDB79E')
    Balance.grid(row=2, column=6)
    Coupon = Label(ReportAssembly, text="Coupon |", bg='#CDB79E')
    Coupon.grid(row=2, column=7)
    Maturity = Label(ReportAssembly, text="Maturity |", bg='#CDB79E')
    Maturity.grid(row=2, column=8)
    Counter = Label(ReportAssembly, text="Position Count", bg='#CDB79E')
    Counter.grid(row=2, column=9)

    #CurrentAccount
    Currentbalance = SQLQuery();Currentbalance=Currentbalance.getbalance("Current Account",dateClick.get(),"Liability")
    Currentcoupon = SQLQuery();Currentcoupon = Currentcoupon.getcoupon("Current Account",dateClick.get(),"Liability")
    Currentmaturity = SQLQuery();Currentmaturity = Currentmaturity.getmaturity("Current Account",dateClick.get(),"Liability")
    Currentcount = SQLQuery();Currentcount = Currentcount.getquantity("Current Account",dateClick.get(),"Liability")

    Instrument = Label(ReportAssembly, text="Checking", bg='#CDB79E')
    Instrument.grid(row=3, column=5)
    Balance = Label(ReportAssembly, text=Currentbalance, bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=3, column=6)
    Coupon = Label(ReportAssembly, text=Currentcoupon, bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=3, column=7)
    Maturity = Label(ReportAssembly, text=Currentmaturity, bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=3, column=8)
    Count = Label(ReportAssembly, text=Currentcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=3, column=9)

    #CD
    CDbalance = SQLQuery();CDbalance=CDbalance.getbalance("Certificate of Deposit",dateClick.get(),"Liability")
    CDcoupon = SQLQuery();CDcoupon = CDcoupon.getcoupon("Certificate of Deposit",dateClick.get(),"Liability")
    CDmaturity = SQLQuery();CDmaturity = CDmaturity.getmaturity("Certificate of Deposit",dateClick.get(),"Liability")
    CDcount = SQLQuery();CDcount = CDcount.getquantity("Certificate of Deposit",dateClick.get(),"Liability")

    Instrument = Label(ReportAssembly, text="CD", bg='#CDB79E')
    Instrument.grid(row=4, column=5)
    Balance = Label(ReportAssembly, text=CDbalance, bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=4, column=6)
    Coupon = Label(ReportAssembly, text=CDcoupon, bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=4, column=7)
    Maturity = Label(ReportAssembly, text=CDmaturity, bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=4, column=8)
    Count = Label(ReportAssembly, text=CDcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=4, column=9)

    #Wholesale
    WHOLEbalance = SQLQuery();WHOLEbalance=WHOLEbalance.getbalance("Wholesale",dateClick.get(),"Liability")
    WHOLEcoupon = SQLQuery();WHOLEcoupon = WHOLEcoupon.getcoupon("Wholesale",dateClick.get(),"Liability")
    WHOLEmaturity = SQLQuery();WHOLEmaturity = WHOLEmaturity.getmaturity("Wholesale",dateClick.get(),"Liability")
    WHOLEcount = SQLQuery();WHOLEcount = WHOLEcount.getquantity("Wholesale",dateClick.get(),"Liability")

    Instrument = Label(ReportAssembly, text="Wholesale", bg='#CDB79E')
    Instrument.grid(row=5, column=5)
    Balance = Label(ReportAssembly, text=WHOLEbalance, bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=5, column=6)
    Coupon = Label(ReportAssembly, text=WHOLEcoupon, bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=5, column=7)
    Maturity = Label(ReportAssembly, text=WHOLEmaturity, bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=5, column=8)
    Count = Label(ReportAssembly, text=WHOLEcount, bg='#CDB79E',fg='#0101DF')
    Count.grid(row=5, column=9)

    Instrument = Label(ReportAssembly, text="", bg='#CDB79E')
    Instrument.grid(row=6, column=5)
    Balance = Label(ReportAssembly, text="", bg='#CDB79E',fg='#0101DF')
    Balance.grid(row=6, column=6)
    Coupon = Label(ReportAssembly, text="", bg='#CDB79E',fg='#0101DF')
    Coupon.grid(row=6, column=7)
    Maturity = Label(ReportAssembly, text="", bg='#CDB79E',fg='#0101DF')
    Maturity.grid(row=6, column=8)
    Count = Label(ReportAssembly, text="", bg='#CDB79E',fg='#0101DF')
    Count.grid(row=6, column=9)

    #Equity
    Equitybalance = SQLQuery();Equitybalance=Equitybalance.getbalance("Equity",dateClick.get(),"Equity")
    Equitycoupon = SQLQuery();Equitycoupon = Equitycoupon.getcoupon("Equity",dateClick.get(),"Equity")
    Equitymaturity = SQLQuery();Equitymaturity = Equitymaturity.getmaturity("Equity",dateClick.get(),"Equity")
    Equitycount = SQLQuery();Equitycount = Equitycount.getquantity("Equity",dateClick.get(),"Equity")

    Instrument = Label(ReportAssembly, text="Equity", bg='#CDB79E')
    Instrument.grid(row=7, column=5)
    Balance = Label(ReportAssembly, text=Equitybalance, bg='#CDB79E',fg='#088A08')
    Balance.grid(row=7, column=6)
    Coupon = Label(ReportAssembly, text=Equitycoupon, bg='#CDB79E',fg='#088A08')
    Coupon.grid(row=7, column=7)
    Maturity = Label(ReportAssembly, text=Equitymaturity, bg='#CDB79E',fg='#088A08')
    Maturity.grid(row=7, column=8)
    Count = Label(ReportAssembly, text=Equitycount, bg='#CDB79E',fg='#088A08')
    Count.grid(row=7, column=9)

    #NET EXPOSURE REPORT
    Netposition = LabelFrame(PositionFrame,text = "Net Exposure Report", padx=5, pady=5, bg='#CDB79E')
    Netposition.grid(row=3, column=0, padx=5, pady=5)

    Instrument = Label(Netposition, text="Instrument |", bg='#CDB79E')
    Instrument.grid(row=2, column=0)
    Balance = Label(Netposition, text="Balance MM |", bg='#CDB79E')
    Balance.grid(row=2, column=1)
    Coupon = Label(Netposition, text="Coupon |", bg='#CDB79E')
    Coupon.grid(row=2, column=2)
    Maturity = Label(Netposition, text="Maturity |", bg='#CDB79E')
    Maturity.grid(row=2, column=3)
    Counter = Label(Netposition, text="Position Count", bg='#CDB79E')
    Counter.grid(row=2, column=4)


def ReviewPositions():
    # Assembly of main frame
    global PositionFrame
    PositionFrame = Tk()
    PositionFrame.geometry("800x400")
    PositionFrame.config(background='#FAEBD7')

    # Assembly of LabelFrame
    global PositionAssembly
    PositionAssembly = LabelFrame(PositionFrame, text="Position Review", padx=5, pady=5, bg='#CDB79E')
    PositionAssembly.grid(row=1, column=0, padx=5, pady=5)

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

    selectInstrument = Button(PositionAssembly, text="Generate Report", command=Report)
    selectInstrument.grid(row=1, column=0,columnspan=3,padx=5, pady=5)
    selectInstrument.config(highlightbackground='#FAEBD7')