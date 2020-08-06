from dateutil.relativedelta import *

class CashFlowForecast:

    def FixedBullet(self,principal,currentDate,maturity,coupon,product,aclass,bcktid):

        from datetime import datetime,date,timedelta

        maturity = datetime.strptime(maturity,'%Y-%m-%d %H:%M:%S')
        rundate = datetime.strptime(currentDate,'%Y-%m-%d %H:%M:%S')

        CFarray = [];ipay=0;ppay=0;period=0
        while maturity>rundate:
            ipay = principal * coupon/100/12
            ppay = 0
            rundate = rundate + relativedelta(months=+1)
            CFarray.append([product,aclass,bcktid,principal,ipay,ppay,rundate,coupon,period]);period+=1

        ipay = principal * coupon/100/12; ppay = principal

        CFarray.append([product,aclass,bcktid,principal,ipay,ppay,rundate,coupon,period])

        return CFarray

    def FixedAmort(self, principal, currentDate, maturity, coupon, product, aclass, bcktid):

        from datetime import datetime, date, timedelta

        maturity = datetime.strptime(maturity, '%Y-%m-%d %H:%M:%S')
        rundate = datetime.strptime(currentDate, '%Y-%m-%d %H:%M:%S')

        r = relativedelta(maturity,rundate)
        n = r.months + (12 * r.years)

        CFarray = [];
        ipay = 0;
        ppay = 0;
        period = 0
        tot_payment = principal*((coupon/1200)*(1+coupon/1200)**n)/(((1+coupon/1200)**n)-1)

        while (maturity > rundate) and (principal>0):
            ipay = principal * coupon / 100 / 12
            ppay = tot_payment-ipay
            principal = principal - ppay
            rundate = rundate + relativedelta(months=+1)
            CFarray.append([product, aclass, bcktid,principal, ipay, ppay, rundate, coupon, period]);
            period += 1
        return CFarray

sample = CashFlowForecast()
sample=sample.FixedAmort(200000,'2020-07-29 00:00:00','2022-07-01 00:00:00',5,'Wholesale','Asset',1)

for i in sample:
    print(i)
