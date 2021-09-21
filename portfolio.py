import pandas as pd
from pandas_datareader import data as web
from datetime import datetime, timedelta
from scipy import stats
import numpy as np
import math

class Portfolio:
    portfolioName = "";
    noOfStock = int(0)
    account_value = float(0)
    invested = float(0)
    turnover = float(0)
    PandL = float(0)
    portf = pd.DataFrame(columns=['Date','Stock','Price','No. of transaction','Value','Average Return(1yr)','Volatility(1yr)','Current Value','Spot Price',"%change"])
    history = pd.DataFrame(columns=['Date','Stock','Action','Price','No. of Transaction'])
    incomeStatrment = pd.DataFrame(columns=['Portfolio Name','Portfolio Expected Return','Portfolio Return','Portfolio Risk'])

    def __init__(self,portfolio_name,account_value):
        self.account_value = account_value
        self.portfolioName = portfolio_name

    def buyStock(self, date, stock, price, noOfTransaction):
        filt = self.portf['Stock'] == stock
        if(self.portf.loc[filt,'Stock'].any()):
            self.invested += price*noOfTransaction

            self.portf.loc[filt,'Price'] = (self.portf.loc[filt,'Value'] + noOfTransaction*price)/(noOfTransaction+self.portf.loc[filt,'No. of transaction'])
            self.portf.loc[filt,'No. of transaction'] = noOfTransaction+self.portf.loc[filt,'No. of transaction']
            self.portf.loc[filt,'Value'] = self.portf.loc[filt,'Price']*self.portf.loc[filt,'No. of transaction']
        else:
            self.noOfStock += 1
            self.invested += price*noOfTransaction
            yearAgo = (datetime.today()- timedelta(365)).strftime('%Y-%m-%d')
            today = datetime.today().strftime('%Y-%m-%d')
            try:
                df = web.DataReader(stock, data_source='yahoo',start= yearAgo,end= today)['Adj Close']
            except:
                print('Invalid Input')
                
            risk = str(round((self.volatility(stock,df))*100,2)) + '%'
            AverageReturn = str(round((self.AverageReturn(stock,df)-1)*100,2)) + '%'
            self.portf.loc[self.noOfStock-1] = [date,stock,float(price),int(noOfTransaction),float(price*noOfTransaction),AverageReturn,risk,0,0,0]
        self.update(self.portf)
        self.account_value -= price*noOfTransaction
        self.addHistory("Buy",date,stock,price,noOfTransaction)

    def sellStock(self,date,stock,price,noOftransaction):
        filt = self.portf['Stock'] == stock
        if(self.portf.loc[filt,'Stock'].any()):
            self.turnover = price*noOftransaction
            self.PandL = (price-float(self.portf.loc[filt]['Price']))*noOftransaction
            self.portf.loc[filt,'No. of transaction'] -= noOftransaction
            self.portf.loc[filt,'Value'] -= price*noOftransaction
             
            if(int(self.portf.loc[filt,'No. of transaction']) == 0):
                self.portf.drop([self.portf[self.portf['Stock']==stock].index[0]])
            self.account_value += price*noOftransaction
            self.addHistory("Sell",date,stock,price,noOftransaction)
            

    def update(self,df):
        today = datetime.today().strftime('%Y-%m-%d');
        weekAgo = (datetime.today()- timedelta(7)).strftime('%Y-%m-%d')
       
        for stocks in df['Stock']:
            df = web.DataReader(stocks, data_source='yahoo',start= weekAgo,end= today)['Adj Close']
            filt = self.portf['Stock'] == stocks
            self.portf.loc[filt,'Spot Price'] = round(df.iloc[len(df)-1],2)  
            self.portf.loc[filt,'%change'] = str(round(((df.iloc[len(df)-1] / float(self.portf.loc[filt,'Price']))-1)*100,2))+'%'          
            self.portf.loc[filt,'Current Value'] = round(df.iloc[len(df)-1],2) *self.portf.loc[filt,'No. of transaction']
    
    def addHistory(self, action, date, stock, price, noOfTranssaction):
        self.history.loc[len(self.history)] = [date,stock,action,price,noOfTranssaction]
        print(self.history)

    def getPortfolio(self):
        return self.portf

    def AverageReturn(self,stock,df):
        returns = df.pct_change()
        returns = returns+1
        b=returns.iloc[1:].values
        a = stats.gmean(b)
        return a

    def volatility(self,stock,df):
        df = df.pct_change()
        var = df.var()
        risk = math.sqrt(var)
        return risk
    #def getPortfolioDetail(self):
        
