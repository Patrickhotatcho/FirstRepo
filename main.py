from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import Indicator
import portfolio as pf
import stock as s
import portfolioList as pfList 

portf1 = pf.Portfolio("Pat",100000)
portf1.buyStock('2020-01-01','AAPL',0, 0)
portf1.buyStock('2020-02-01','GOOG',0, 0)
portf1.buyStock('2020-03-01','NFLX',0, 0) 

f1 = plt.figure()
ax1 = f1.add_subplot(111)
VMA_20 = Indicator.MovingAverage.Volatility_MA('2020-01-01','NFLX',20)
Indicator.MovingAverage.plotChart("20 days Price MA","NFLX",VMA_20,"-")
f2 = plt.figure()
ax2 = f2.add_subplot(111)
PMA_20 = Indicator.MovingAverage.Price_MA('2020-01-01','NFLX',20)
Indicator.MovingAverage.plotChart("20 days Standard Deviation MA","NFLX",PMA_20,"-")

plt.show()
'''
for i in range(0,len(portf1.portf)-1):
    MA_1= Indicator.MovingAverage.MA('2020-01-01',portf1.portf.loc[i,'Stock'],1)
    a = MA_1.pct_change()
    sd = portf1.portf.loc[i,"Volatility(1yr)"]
    returns = portf1.portf.loc[i,"Average Arithmetic Return(1yr)"]
    for j in range(0,len(MA_1)-1):
        if( a>and portf1.account_value>0):
            portf1.buyStock(MA_1.loc[i,"Date"],'GOOG',float(MA_1.loc[i,"MA"]), 25)

        if( and portf1.portf.loc[i,'No. of transaction']>0):
            portf1.sellStock(MA_1.loc[i,"Date"],'GOOG',float(MA_1.loc[i,"MA"]),25)

        if(portf1.portf.loc[0,'Price']*0.92>MA_1.loc[i+4,"MA"] and portf1.portf.loc[i,'No. of transaction']>0):
            portf1.sellStock(MA_1.loc[i,"Date"],'GOOG',float(MA_1.loc[i,"MA"]),25)
            print("STOP Loss at -8%")
print(portf1.getPortfolio())
print(portf1.getPortfolioDetail())
'''

'''
portf2 = pf.Portfolio("Nat",100000)
portf2.buyStock('2020-01-01','FB',300, 10)
portf2.buyStock('2020-02-01','NIO',30, 50)

print(portf2.getPortfolio())
print(portf2.getPortfolioDetail())
print(portf1.getPortfolio())
portfList = pfList.portfolioList('pl1')
portfList.addPortfolio(portf1)
portfList.addPortfolio(portf2)
'''
'''
MA_1 = Indicator.MovingAverage.MA('2020-02-01','GOOG',1)
MA_5 = Indicator.MovingAverage.MA('2020-02-01','GOOG',5)
MA_20 = Indicator.MovingAverage.MA('2020-02-01','GOOG',20)
portf3 = pf.Portfolio("Pat",100000)
portf3.buyStock('2020-01-01','GOOG',0, 0)
for i in range(0,len(MA_5)-1):
    if(int(MA_1.loc[i+4,"MA"])<=int(MA_5.loc[i,"MA"]*1.01) and int(MA_1.loc[i+4,"MA"])>=int(MA_5.loc[i,"MA"]) and int(MA_1.loc[i+5,"MA"])<int(MA_5.loc[i+1,"MA"]) and portf3.account_value>0):
        portf3.buyStock(MA_1.loc[i,"Date"],'GOOG',float(MA_1.loc[i,"MA"]), 25)

    if(int(MA_1.loc[i+4,"MA"] )<=int(MA_1.loc[i,"MA"]*1.01 ) and int(MA_1.loc[i+4,"MA"])>=int(MA_5.loc[i,"MA"]) and int(MA_1.loc[i+5,"MA"])>int(MA_5.loc[i+1,"MA"]) and portf3.portf.loc[0,'No. of transaction']>0):
        portf3.sellStock(MA_1.loc[i,"Date"],'GOOG',float(MA_1.loc[i,"MA"]),25)

    if(portf3.portf.loc[0,'Price']*0.92>MA_1.loc[i+4,"MA"] and portf3.portf.loc[0,'No. of transaction']>0):
        portf3.sellStock(MA_1.loc[i,"Date"],'GOOG',float(MA_1.loc[i,"MA"]),25)
        print("STOP Loss at -8%")

print(portf3.getPortfolio())
print(portf3.getPortfolioDetail()) 
'''
'''Indicator.MovingAverage.plotChart("5 days Moving Average",MA_5,"b--")
Indicator.MovingAverage.plotChart("20 days Moving Average",MA_1,"-")
Indicator.MovingAverage.plotChart("20 days Moving Average",MA_20,"r--")

plt.show()'''