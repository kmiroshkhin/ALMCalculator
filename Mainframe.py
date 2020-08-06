from MarketDownload import LoadMarketInitiation
from YieldCurveGeneration import *
from PositionGenerator import *
from PositionReview import *
from ALMCalculator.Frames.CashflowProjection import *

global Mainframe

Mainframe = Tk()

Mainframe.geometry('700x300')
Mainframe.config(background='#FAEBD7')

# LEFT FRAME with configuration widgets to be positioned under
Configurationframe = LabelFrame(Mainframe, text='Configuration', padx=5, pady=5, bg='#FAEBD7')
Configurationframe.grid(row=0, column=0, padx=5, pady=5)

# Market Frame with market configuration activities to be positioned under
Marketframe = LabelFrame(Configurationframe, text='Market frame', padx=80, pady=10, bg='#CDB79E')
Marketframe.grid(row=0, column=0, padx=5, pady=5)

# Market Frame Button Placements
LoadMarketButton = Button(Marketframe, text='Load Market', highlightbackground='#CDB79E', command=LoadMarketInitiation)
LoadMarketButton.grid(row=0, column=0, padx=1, pady=1)

YieldCurveGeneratorButton = Button(Marketframe, text='Generate Yield Curve', highlightbackground='#CDB79E',
                                   command=YieldCurveGeneration)
YieldCurveGeneratorButton.grid(row=1, column=0, padx=1, pady=1)

# Market Frame with market configuration activities to be positioned under
Positionframe = LabelFrame(Configurationframe, text='Position frame', padx=87, pady=10, bg='#CDB79E')
Positionframe.grid(row=1, column=0, padx=5, pady=5)

# Position Frame Button Placements
PositionGeneratorButton = Button(Positionframe, text='Generate Positions', highlightbackground='#CDB79E',
                                 command=GeneratePosition)
PositionGeneratorButton.grid(row=0, column=0, padx=1, pady=1)

PositionReviewButton = Button(Positionframe, text='Position Review', highlightbackground='#CDB79E', command = ReviewPositions)
PositionReviewButton.grid(row=1, column=0, padx=1, pady=1)

# Analytics Frame with analytics configuration activities to be positioned under
Analyticsframe = LabelFrame(Configurationframe, text='Analytics', padx=85, pady=10, bg='#CDB79E',
                            highlightbackground='#CDB79E')
Analyticsframe.grid(row=0, column=1, padx=5, pady=5)

# Analytics Frame Button Placements
EVEAnalyticsButton = Button(Analyticsframe, text='EVE Calculator', highlightbackground='#CDB79E')
EVEAnalyticsButton.grid(row=0, column=0, padx=1, pady=1)

CashflowgeneratorButton = Button(Analyticsframe, text='Cash Flow Forecast', highlightbackground='#CDB79E',command=CF_Forecast)
CashflowgeneratorButton.grid(row=1, column=0, padx=1, pady=1)

# Report Frame reporting activities to be positioned under
ReportingFrame = LabelFrame(Configurationframe, text='Reporting', padx=83, pady=25, bg='#CDB79E')
ReportingFrame.grid(row=1, column=1, padx=5, pady=5)

# Report Frame Button Placements
ReportingButton = Button(ReportingFrame, text='Reporting Generator', highlightbackground='#CDB79E')
ReportingButton.grid(row=0, column=0, padx=1, pady=1)

Mainframe.mainloop()
