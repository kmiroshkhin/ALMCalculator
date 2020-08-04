class InstrumentGenerator:

    def __init__(self,portfoliobalance,individualmaxbalance,coupon,InstrumentName,AL,Amortization,portfolioDate,maturity):
        import random,datetime as dt,time

        time.time()

        port_dtl = [];cumBal=0;n=1

        while portfoliobalance>=cumBal:
            self.coupon = coupon + random.randrange(-200,200,10,int)/100
            self.principal = random.randrange(0,individualmaxbalance)

            #Frequency definition
            if random.randrange(0,3)<1:
                self.frq = 'monthly'
            elif random.randrange(0,3)<2:
                self.frq = 'quarterly'
            else: self.frq = 'Annual'


            self.AL = AL
            self.portfolioDate = dt.datetime.strptime(portfolioDate,'%Y-%m-%d')
            self.maturity = self.portfolioDate + dt.timedelta(days=random.randrange(0,maturity*365))
            self.instrumentName = InstrumentName
            self.amortization = Amortization
            self.bcktid = n; n+=1
            port_dtl.append([self.principal,self.coupon,self.frq,self.instrumentName,self.AL,self.amortization,self.portfolioDate,self.maturity,self.bcktid])
            cumBal+=self.principal
        self.output = port_dtl