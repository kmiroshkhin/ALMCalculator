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
