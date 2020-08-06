import sqlite3

class SQLQuery:
    def distinctmrktdates(self):
        conn = sqlite3.connect('C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT distinct date from MarketRates")
        retrieval = c.fetchall()
        c.close()
        newlist =[]
        for record in retrieval:
            newlist.append(record[0])

        return newlist

    def distinctproductassetclass(self,portfoliodate):
        conn = sqlite3.connect('C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT distinct productName,assetClass from portbckt where portfoliodate = "+ "'"+ portfoliodate + "'")
        retrieval = c.fetchall()
        c.close()
        return retrieval

    def getbalance(self,product,date,aclass):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
        "SELECT sum(balance) from portbckt where portfoliodate = "+"'"+date+"'"+ "and productName ="+"'"+product+"'"+ " and assetclass ="+"'"+aclass+"'")
        retrieval = c.fetchall()
        c.close()

        try: return round(retrieval[0][0]/1000000,2)
        except: return 0

    def getcoupon(self,product,date,aclass):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT sum(balance * coupon)/sum(balance) from portbckt where portfoliodate = " + "'" + date + "'" + "and productName =" + "'"+product+"'"+ " and assetclass ="+"'"+aclass+"'")
        retrieval = c.fetchall()
        c.close()

        try: return round(retrieval[0][0], 2)
        except: return 0

    def getquantity(self,product,date,aclass):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT COUNT (*) from portbckt where portfoliodate = " + "'" + date + "'" + " and productName = " +"'"+ product+"'"+ " and assetclass ="+"'"+aclass+"'")
        retrieval = c.fetchall()[0][0]
        c.close()

        return retrieval

    def totalcount(self,date):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT COUNT (*) from portbckt where portfoliodate = " + "'" + date + "'")
        retrieval = c.fetchall()[0][0]
        c.close()

        return retrieval


    def getmaturity(self,product,date,aclass):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT maturitydate,portfoliodate,balance from portbckt where portfoliodate = " + "'" + date + "'" + "and productName =" + "'" +product+"'"+ " and assetclass ="+"'"+aclass+"'")
        retrieval = c.fetchall()

        from datetime import date
        incbalance=0;daydeltabalance=0
        for output in retrieval:
            matyear = output[0][0:4];matmonth =output[0][5:7];matdate = output[0][8:10]
            poryear = output[1][0:4];pormonth =output[1][5:7];pordate = output[1][8:10]

            mat=date(int(matyear),int(matmonth),int(matdate))
            por=date(int(poryear),int(pormonth),int(pordate))
            daydelta = mat-por;daybaldel = int(daydelta.days)*int(output[2])

            incbalance += int(output[2]); daydeltabalance += daybaldel

        try: return round(daydeltabalance/incbalance/365,2)
        except: return 0

        c.close()


    def distinctportfoliodates(self):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT distinct portfoliodate from portbckt")
        retrieval = c.fetchall()
        c.close()
        newlist = []
        for record in retrieval:
            newlist.append(record[0])

        return newlist

    def NetBalanceExposure(self,date):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT sum(balance) from portbckt where assetclass = 'Asset' and portfoliodate = "+"'"+date+"'")
        assetsize = c.fetchall()
        c.execute(
            "SELECT sum(balance) from portbckt where assetclass in ('Liability','Equity') and portfoliodate = " + "'" + date + "'")
        liabilitysize = c.fetchall()
        c.close()

        return round((assetsize[0][0]-liabilitysize[0][0])/1000000,2)

    def NetCouponExposure(self,date):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT sum(balance*coupon)/sum(balance) from portbckt where assetclass = 'Asset' and portfoliodate = "+"'"+date+"'")
        assetWAC = c.fetchall()[0][0]
        c.execute("SELECT sum(balance) from portbckt where assetclass = 'Asset' and portfoliodate = " + "'" + date + "'")
        assetbalance = c.fetchall()[0][0]
        c.execute(
            "SELECT sum(balance*coupon)/sum(balance) from portbckt where assetclass in ('Liability','Equity') and portfoliodate = " + "'" + date + "'")
        liabilityWAC = c.fetchall()[0][0]
        c.execute(
            "SELECT sum(balance) from portbckt where assetclass in ('Liability','Equity') and portfoliodate = " + "'" + date + "'")
        liabilitybalance = c.fetchall()[0][0]
        c.close()
        TotBal = assetbalance+liabilitybalance; NIM=(assetbalance/TotBal*assetWAC)-(liabilitybalance/TotBal*liabilityWAC)

        return round(NIM*2,2)

    def maturitydelta(self,day):
        conn = sqlite3.connect(
            'C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()
        c.execute(
            "SELECT maturitydate,portfoliodate,balance from portbckt where portfoliodate = " + "'" + day + "'" + " and assetclass in ('Asset')")
        assetmaturity = c.fetchall()

        from datetime import date
        incbalance=0;assetdaydeltabalance=0
        for output in assetmaturity:
            matyear = output[0][0:4];matmonth =output[0][5:7];matdate = output[0][8:10]
            poryear = output[1][0:4];pormonth =output[1][5:7];pordate = output[1][8:10]

            mat=date(int(matyear),int(matmonth),int(matdate))
            por=date(int(poryear),int(pormonth),int(pordate))
            daydelta = mat-por;daybaldel = int(daydelta.days)*int(output[2])

            incbalance += int(output[2]); assetdaydeltabalance += daybaldel

        assetlength = round(assetdaydeltabalance/incbalance/365,2)

        c.execute(
            "SELECT maturitydate,portfoliodate,balance from portbckt where assetclass in ('Liability','Equity') and"
            " portfoliodate = " + "'" + day + "'")

        liabilitymaturity = c.fetchall()

        from datetime import date
        incbalance = 0;
        liabilitydaydeltabalance = 0
        for output in liabilitymaturity:
            matyear = output[0][0:4];
            matmonth = output[0][5:7];
            matdate = output[0][8:10]
            poryear = output[1][0:4];
            pormonth = output[1][5:7];
            pordate = output[1][8:10]

            mat = date(int(matyear), int(matmonth), int(matdate))
            por = date(int(poryear), int(pormonth), int(pordate))
            daydelta = mat - por;
            daybaldel = int(daydelta.days) * int(output[2])

            incbalance += int(output[2]);
            liabilitydaydeltabalance += daybaldel

        liabilitylength = round(liabilitydaydeltabalance / incbalance / 365, 2)
        c.close()

        return round(assetlength - liabilitylength,2)

    def insertrecords(self,list):
        conn = sqlite3.connect('C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()

        try:
            c.execute("""
        CREATE TABLE portbckt (
            balance REAL,
            coupon REAL,
            resetFrq text,
            productName text,
            assetclass text,
            amortization text,
            portfoliodate text,
            maturitydate text,
            bucketID text
            )""")
        except:
            print('table already exists')
        conn.commit()
        conn.close()

        conn = sqlite3.connect('C:/Users/16195/Desktop/Coding Projects/Python/Application/ALMCalculator/Frames/financial_Calculator.db')
        c = conn.cursor()

        for entry in list:
            c.execute("INSERT INTO portbckt VALUES (:bal,:cpn,:rstfq,:prodn,:assclass,:amrt,:portdate,:mature,:bcktid)",
                      {
                          'bal': entry[0],
                          'cpn': entry[1],
                          'rstfq': entry[2],
                          'prodn': entry[3],
                          'assclass':entry[4],
                          'amrt': entry[5],
                          'portdate': entry[6],
                          'mature': entry[7],
                          'bcktid': entry[8]

                      })

            # Commit changes
            conn.commit()

getdate = SQLQuery()
getdate = getdate.distinctportfoliodates()[2]
print(getdate)

count = SQLQuery()
count = count.distinctproductassetclass(getdate)

for i in count:
    print(i)