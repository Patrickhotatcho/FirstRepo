from textwrap import wrap
from numpy.lib.function_base import append
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import sqlite3
import sqlalchemy
from sqlalchemy.sql.expression import true
from tkinter import *
import Indicator
import portfolio as pf
import stock as s
import portfolioList as pfList 
from tkinter import ttk


def load(dataset):
    
    for i in range(0,len(dataset)):
        tv.insert("","end",value=(dataset.loc[i,'Portfolio Name'],dataset.loc[i,'Portfolio Expected Return(1yr)'],dataset.loc[i,'Portfolio Risk'],dataset.loc[i,'Profit and Loss'],dataset.loc[i,'Invested Money'],dataset.loc[i,'Cash'],dataset.loc[i,'Current Portfolio Return'],dataset.loc[i,'Profit Trade'],dataset.loc[i,'Loss Trade']))
    


 
root = Tk()

engine = sqlalchemy.create_engine('mysql+pymysql://root:@Password@localhost:3306/portfolio')

df = pd.read_sql('portfolio list',engine)
print(df)
wrapper1 = LabelFrame(root,text='Portfolio List')
wrapper1.pack(fill='both',expand='yes',padx=20,pady=10)
tv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9), show='headings',height=str(len(df)))
tv.pack();

tv.heading(1,text='Portfolio Name')
tv.heading(2,text='Portfolio Expected Return(1yr)')
tv.heading(3,text='Portfolio Risk')
tv.heading(4,text='Profit and Loss')
tv.heading(5,text='Invested Money')
tv.heading(6,text='Cash')
tv.heading(7,text='Current Portfolio Return')
tv.heading(8,text='Profit Trade')
tv.heading(9,text='Loss Trade')
load(df)

wrapper2 = LabelFrame(root,text='Create Portfolio')
wrapper2.pack(fill='both',expand='yes',padx=20,pady=10)


root.title('Portfolio')
root.geometry('800x700')
root.mainloop()

'''
engine = sqlalchemy.create_engine('mysql+pymysql://root:@Password@localhost:3306/portfolio')
df = pd.read_sql('portfolio',engine)
portf1 = pf.Portfolio("Pat",100000)



portf1.buyStock('2020-01-01','AAPL',180, 23)
portf1.buyStock('2020-02-01','GOOG',1800, 23)
portf1.buyStock('2020-03-01','NFLX',120, 23) 
print(portf1.getPortfolio())
print(portf1.getPortfolioDetail())

portf1.getPortfolio().to_sql(name='portfolio',con=engine,index=true,if_exists='replace')
portf1.getPortfolioDetail().to_sql(name='portfolio list',con=engine,index=true,if_exists='replace')
'''



'''
MA_1 = Indicator.MovingAverage.Price_MA('2020-02-01','GOOG',1)
MA_5 = Indicator.MovingAverage.Price_MA('2020-02-01','GOOG',5)
MA_20 = Indicator.MovingAverage.Price_MA('2020-02-01','GOOG',20)
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