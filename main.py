from os import replace
from textwrap import wrap
from numpy.lib.function_base import append, select
from pandas_datareader import data as web, test
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import sqlite3
from sqlalchemy import *
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import false, true
from tkinter import *
import Indicator
import portfolio as pf
import stock as s
import portfolioList as pfList 
from tkinter import ttk 
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine('mysql+pymysql://root:@Password@localhost:3306/portfolio')
Sesssion = sessionmaker(engine)
session = Session()
meta = MetaData(bind=engine)
Base = declarative_base()
class portfolio_list(Base):
    __tablename__ = 'portfolio_list'
    Portfolio_Name = Column(String(10),primary_key=true)
    Portfolio_Expected_Return = Column(String(10))
    Portfolio_Risk = Column(String(10))
    Profit_and_Loss = Column(Float)
    Invested_Money = Column(String(10))
    Cash = Column(Float)
    Current_Portfolio_Return = Column(String(10))
    Profit_Trade = Column(INT)
    Loss_Trade = Column(INT)

    
Base.metadata.create_all(engine)

def loadtv(dataset):
    
    for i in range(0,len(dataset)):
        tv.insert("","end",value=(dataset.loc[i,'Portfolio_Name'],dataset.loc[i,'Portfolio_Expected_Return'],dataset.loc[i,'Portfolio_Risk'],dataset.loc[i,'Profit_and_Loss'],dataset.loc[i,'Invested_Money'],dataset.loc[i,'Cash'],dataset.loc[i,'Current_Portfolio_Return'],dataset.loc[i,'Profit_Trade'],dataset.loc[i,'Loss_Trade']))

def loadtv2(dataset):
    
    for i in range(0,len(dataset)):
        tv2.insert("","end",value=(dataset.loc[i,'Date'],dataset.loc[i,'Stock'],dataset.loc[i,'Price'],dataset.loc[i,'No. of transaction'],dataset.loc[i,'Value'],dataset.loc[i,'Average Geometric Return(1yr)'],dataset.loc[i,'Average Arithmetric Return(1yr)'],dataset.loc[i,'Volatility(1yr)'],dataset.loc[i,'Current Value'],dataset.loc[i,'Spot Price'],dataset.loc[i,'%change']))

def DoubleClick(event):
    selected = tv.selection()
    value = tv.item(selected,'values')
    df = pd.read_sql(str(value[0]),engine)


def click_CP():
    porName = e_CP_N.get()
    porValue = e_CP_V.get()
    portf = pf.Portfolio(porName,porValue)
    portf.getPortfolioDetail().to_sql(name='portfolio_list',con=engine,if_exists='append',index=false)
    df = pd.read_sql('portfolio_list',engine)
    tv.insert("","end",value=(df.loc[len(df)-1,'Portfolio_Name'],df.loc[len(df)-1,'Portfolio_Expected_Return'],df.loc[len(df)-1,'Portfolio_Risk'],df.loc[len(df)-1,'Profit_and_Loss'],df.loc[len(df)-1,'Invested_Money'],df.loc[len(df)-1,'Cash'],df.loc[len(df)-1,'Current_Portfolio_Return'],df.loc[len(df)-1,'Profit_Trade'],df.loc[len(df)-1,'Loss_Trade']))
    portfo =  Table(porName,meta,Column('Date',DateTime),Column('Stock',String(10),primary_key=true),Column('Price',Float),Column('No. of transaction',INT),Column('Value',Float),Column('Average Geometric Return(1yr)',String(10)),Column('Average Arithmetric Return(1yr)',String(10)),Column('Volatility(1yr)',String(10)),Column('Current Value',Float),Column('Spot Price',Float),Column('%change',String(10)))
    meta.create_all(engine)

def click_RP():
    selected = tv.selection()[0]
    item = tv.focus()
    pn = tv.item(item).get('values')
    
    tv.delete(selected)
    Session = sessionmaker(bind=engine)
    session = Session()
    record_obj = session.query(portfolio_list).filter(portfolio_list.Portfolio_Name == pn[0]).one()
    session.delete(record_obj)
    session.commit()
    session.close()
    portf = Table(pn[0],meta,autoload_with=engine)
    Base.metadata.drop_all(bind=engine, tables=[portf.__table__])
    #record_obj = session.query("portfolio list").filter()
    

root = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")



df = pd.read_sql('portfolio_list',engine)
print(df)
wrapper1 = LabelFrame(root,text='Portfolio List')
wrapper1.pack(fill='both',expand='yes',padx=20,pady=10)
tv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9), show='headings',height=str(15))
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
for i in range(0,10):
    tv.column(i,width=145)
loadtv(df)

tv.bind("<Double-1>", DoubleClick)
b_CP = Button(wrapper1,text='Create Portfolio',command=click_CP)
b_CP.place(x=20,y=380)
e_CP_N = Entry(wrapper1)
e_CP_N.place(x=250,y=382)
l_CP_N = Label(wrapper1,text='Portfolio Name')
l_CP_N.place(x=135,y=382)

e_CP_V = Entry(wrapper1)
e_CP_V.place(x=550,y=382)
l_CP_V = Label(wrapper1,text='Portfolio Value')
l_CP_V.place(x=435,y=382)

b_RP = Button(wrapper1,text='Remove Portfolio',command=click_RP)
b_RP.place(x=1000,y=382)

#df2 = pd.read_sql('pat',engine)
wrapper2 = LabelFrame(root,text='Portfolio')
wrapper2.pack(fill='both',expand='yes',padx=20,pady=10)
tv2 = ttk.Treeview(wrapper2,columns=(1,2,3,4,5,6,7,8,9,10,11), show='headings',height='10')
tv2.pack();
tv2.heading(1,text='Date')
tv2.heading(2,text='Stock')
tv2.heading(3,text='Price')
tv2.heading(4,text='No. of transaction')
tv2.heading(5,text='Value')
tv2.heading(6,text='Average Geometric Return(1yr)')
tv2.heading(7,text='Average Arithmetric Return(1yr)')
tv2.heading(8,text='Volatility(1yr)')
tv2.heading(9,text='Current Value')
tv2.heading(10,text='Spot Price')
tv2.heading(11,text='%change')



root.title('Portfolio')
root.geometry('1400x1000')
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