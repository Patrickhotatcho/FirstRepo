import pandas as pd
from pandas_datareader import data as web
from datetime import datetime, timedelta
from scipy import stats
import numpy as np
import math

class Portfolio:
    noOfStock = 0;
    totalValue = 0;

    portf = pd.DataFrame(columns=['Date','Stock','Price','No. of transaction','Value','Average Return','Volatility','Current Value'])

    def __init__(self):
        self.totalValue = 0;
        self.noOfStock = 0;

    def addStock(self, date, stock, price, noOfTransaction):   
        yearAgo = (datetime.today()- timedelta(365)).strftime('%Y-%m-%d')
        today = datetime.today().strftime('%Y-%m-%d')
        try:
            df = web.DataReader(stock, data_source='yahoo',start= yearAgo,end= today)['Adj Close']
        except:
            print('Invalid Input')
        
        self.noOfStock += 1
        self.totalValue += price*noOfTransaction
        risk = str(round((self.volatility(stock,df))*100,2)) + '%'
        AverageReturn = str(round((self.AverageReturn(stock,df)-1)*100,2)) + '%'
        self.portf.loc[self.noOfStock-1] = [date,stock,price,noOfTransaction,(price*noOfTransaction),AverageReturn,risk,0]
        self.updateCurrentValue(self.portf)

    def updateCurrentValue(self,df):
        today = datetime.today().strftime('%Y-%m-%d');
        weekAgo = (datetime.today()- timedelta(7)).strftime('%Y-%m-%d')
       
        for stocks in df['Stock']:
            df = web.DataReader(stocks, data_source='yahoo',start= weekAgo,end= today)['Adj Close']
            filt = self.portf['Stock'] == stocks
            self.portf.loc[filt,'Current Value'] = df.iloc[len(df)-1]*self.portf.loc[filt,'No. of transaction']

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

