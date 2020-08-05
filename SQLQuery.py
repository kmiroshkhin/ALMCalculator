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
getdate = getdate.distinctportfoliodates()[0]
print(getdate)

getquantity = SQLQuery()
getquantity = getquantity.getquantity('Cash',getdate,'Asset')

print(getquantity)