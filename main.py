from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import Indicator
import portfolio as pf
import stock as s
  

'''portf1 = pf.Portfolio("Pat",100000000)
portf1.buyStock('2020-01-01','AAPL',130, 1000)
portf1.buyStock('2020-02-01','GOOG',200, 500)
portf1.buyStock('2020-03-01','NFLX',120, 500)
portf1.buyStock('2020-03-01','NFLX',110, 500)
portf1.buyStock('2020-03-01','NFLX',160, 500)
portf1.sellStock('2020-03-01','AAPL',150,200)
portf1.sellStock('2020-03-01','AAPL',150,800)
print(portf1.getPortfolio())
print(portf1.getPortfolioDetail())
print(s.stockDetail.getStockLatest("AAPL"))'''

MA_1 = Indicator.MovingAverage.MA('2020-02-01','GOOG',1)
MA_5 = Indicator.MovingAverage.MA('2020-02-01','GOOG',5)
MA_20 = Indicator.MovingAverage.MA('2020-02-01','GOOG',20)
print(MA_5)
portf1 = pf.Portfolio("Pat",100000000)
portf1.buyStock('2020-01-01','GOOG',0, 0)

for i in range(0,len(MA_5)-1):
    if(int(MA_1.loc[i+4,"MA"])<=int(MA_5.loc[i,"MA"]*1.01) and int(MA_1.loc[i+4,"MA"])>=int(MA_5.loc[i,"MA"]) and int(MA_1.loc[i+5,"MA"])<int(MA_5.loc[i+1,"MA"])):
        portf1.buyStock(MA_5.loc[i,"Date"],'GOOG',float(MA_5.loc[i,"MA"]), 100)
    if(int(MA_1.loc[i+4,"MA"])<=int(MA_5.loc[i,"MA"]*1.01) and int(MA_1.loc[i+4,"MA"])>=int(MA_5.loc[i,"MA"]) and int(MA_1.loc[i+5,"MA"])>int(MA_5.loc[i+1,"MA"]) and portf1.portf.loc[0,'No. of transaction']>0):
        portf1.sellStock(MA_5.loc[i,"Date"],'GOOG',float(MA_5.loc[i,"MA"]),100)
print(portf1.getPortfolio())
print(portf1.getPortfolioDetail())   
 
'''Indicator.MovingAverage.plotChart("5 days Moving Average",MA_5,"b--")
Indicator.MovingAverage.plotChart("20 days Moving Average",MA_1,"-")
Indicator.MovingAverage.plotChart("20 days Moving Average",MA_20,"r--")

plt.show()'''