from tkinter import *
from ALMCalculator.Analytics.InstrumentGenerator import *
from ALMCalculator.Analytics.SQLQuery import *

def GeneratePosition():

    def PositionExeuction():
        TotAmt = float(TotalAmountEntry.get())
        maxamt = float(maxAmountEntry.get())
        coupon = float(CouponEntry.get())
        maturity = float(MaturityEntry.get())
        ptype = Productclicked.get()
        atype = AssetClicked.get()
        amort = AmortClicked.get()
        portdate = dateClick.get()

        instGen = InstrumentGenerator(TotAmt,maxamt,coupon,ptype,atype,amort,portdate,maturity)

        for i in instGen.output:
            print(i)
        SQLinsert = SQLQuery()
        SQLinsert.insertrecords(instGen.output)

    #Assembly of main frame
    global PositionFrame
    PositionFrame = Tk()
    PositionFrame.geometry("300x300")
    PositionFrame.config(background='#FAEBD7')


    #Assembly of LabelFrame
    global PositionAssembly
    PositionAssembly = LabelFrame(PositionFrame, text="Position Generator", padx=5, pady=5, bg='#CDB79E')
    PositionAssembly.grid(row=1, column=0, padx=5, pady=5)

    #Total Amount
    TotalAmount = Label(PositionAssembly, text="Total Amount: ", bg='#CDB79E')
    TotalAmount.grid(row=0, column=0)

    TotalAmountEntry = Entry(PositionAssembly)
    TotalAmountEntry.grid(row=0,column=1)

    #Max amount
    maxAmount = Label(PositionAssembly, text="Max Individual Amt: ", bg='#CDB79E')
    maxAmount.grid(row=1, column=0)

    maxAmountEntry = Entry(PositionAssembly)
    maxAmountEntry.grid(row=1,column=1)

    #Coupon Amount
    Coupon = Label(PositionAssembly, text="Coupon (%): ", bg='#CDB79E')
    Coupon.grid(row=2, column=0)

    CouponEntry = Entry(PositionAssembly)
    CouponEntry.grid(row=2,column=1)

    #Maturity
    Maturity = Label(PositionAssembly, text="Maximum Maturity: ", bg='#CDB79E')
    Maturity.grid(row=3, column=0)

    MaturityEntry = Entry(PositionAssembly)
    MaturityEntry.grid(row=3,column=1)

    #ProductType
    ProductType = Label(PositionAssembly, text="Product Type: ", bg='#CDB79E')
    ProductType.grid(row=4, column=0)

    Productclicked = StringVar()
    ProductDrop = OptionMenu(PositionAssembly,Productclicked,"Cash","Mortgage","CRE","C&I","Wholesale","Current Account","Certificate of Deposit","Equity")
    ProductDrop.grid(row=4,column=1)

    #AssetClass
    AssetClass = Label(PositionAssembly, text="Balance Sheet Class: ", bg='#CDB79E')
    AssetClass.grid(row=5, column=0)

    AssetClicked = StringVar()
    AssetClassDrop = OptionMenu(PositionAssembly,AssetClicked,"Asset","Liability","Equity")
    AssetClassDrop.grid(row=5,column=1)
    AssetClassDrop.config(highlightbackground='#FAEBD7')

    #Amortization Schedule
    Amort = Label(PositionAssembly, text="Amortization Schedule: ", bg='#CDB79E')
    Amort.grid(row=6, column=0)

    AmortClicked = StringVar()
    AssetClassDrop = OptionMenu(PositionAssembly,AmortClicked,"Straight-Line","Bullet")
    AssetClassDrop.grid(row=6,column=1)
    AssetClassDrop.config(highlightbackground='#FAEBD7')

    # PortfolioDate

    getdate = SQLQuery()
    getdate = getdate.distinctmrktdates()
    print(getdate)

    Portfolio = Label(PositionAssembly, text="Portfolio Date: ", bg='#CDB79E')
    Portfolio.grid(row=7, column=0)

    dateClick = StringVar()
    PortfolioDrop = OptionMenu(PositionAssembly,dateClick,*getdate)
    PortfolioDrop.grid(row=7,column=1)
    PortfolioDrop.config(highlightbackground='#FAEBD7')

    print(dateClick.get())

    #Generate
    selectInstrument = Button(PositionAssembly, text="Generate Instruments", command=PositionExeuction)
    selectInstrument.grid(row=8, column=0,columnspan=3,padx=5, pady=5)
    selectInstrument.config(highlightbackground='#FAEBD7')