import pandas as pd
from pandas_datareader import data as web
from datetime import datetime, timedelta
from scipy import stats
import numpy as np
import math
import stock as s

class Portfolio:
    portfolioName = "";
    noOfStock = int(0)
    account_value = float(0)
    invested = float(0)
    portfolioValue = float(0)
    turnover = float(0)
    PandL = float(0)
    portf = pd.DataFrame(columns=['Date','Stock','Price','No. of transaction','Value','Average Geomatric Return(1yr)','Average Arithmetic Return(1yr)','Volatility(1yr)','Current Value','Spot Price',"%change"])
    history = pd.DataFrame(columns=['Date','Stock','Action','Price','No. of Transaction'])
    incomeStatrment = pd.DataFrame(columns=['Portfolio Name','Portfolio Expected Return(1yr)','Portfolio Risk','Profit and Loss'])

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
            today = datetime.today().strftime('%Y-%m-%d')
            df = s.stockDetail.getStockData(stock,365,today)
                
            risk = str(round((self.volatility(df))*100,2)) + '%'
            AverageGeomatricReturn = str(round(((self.AverageGeomatricReturn(df)-1))*100,2)) + '%'
            AverageArithmeticReturn = str(round((self.AverageArithmeticReturn(df))*100,2)) + '%'
            self.portf.loc[self.noOfStock-1] = [date,stock,float(price),int(noOfTransaction),float(price*noOfTransaction),AverageGeomatricReturn,AverageArithmeticReturn,risk,0,0,0]
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
        self.update(self.portf)

    def update(self,df):
        today = datetime.today().strftime('%Y-%m-%d');
 
        for stocks in df['Stock']:
            df = s.stockDetail.getStockData(stocks,7,today)
            filt = self.portf['Stock'] == stocks
            self.portf.loc[filt,'Spot Price'] = round(df.iloc[len(df)-1],2)  
            self.portf.loc[filt,'%change'] = str(round(((df.iloc[len(df)-1] / float(self.portf.loc[filt,'Price']))-1)*100,2))+'%'          
            self.portf.loc[filt,'Current Value'] = round(df.iloc[len(df)-1],2) *self.portf.loc[filt,'No. of transaction']
        self.portfolioValue = self.portf['Current Value'].sum()

    def addHistory(self, action, date, stock, price, noOfTranssaction):
        self.history.loc[len(self.history)] = [date,stock,action,price,noOfTranssaction]
        print(self.history)

    def getPortfolio(self):
        return self.portf

    def AverageGeomatricReturn(self,df):
        returns = df.pct_change()
        returns = returns+1
        b=returns.iloc[1:].values
        a = stats.gmean(b)
        return a

    def AverageArithmeticReturn(self,df):
        returns = df.pct_change()
        returns = returns.mean()
        return returns

    def volatility(self,df):
        df = df.pct_change()
        var = df.var()
        risk = math.sqrt(var)
        return risk
    def getPortfolioDetail(self):
        yearAgo = (datetime.today()- timedelta(365)).strftime('%Y-%m-%d')
        today = datetime.today().strftime('%Y-%m-%d')
        df = pd.DataFrame()
        for stock in self.portf['Stock']:
            df[stock] = web.DataReader(stock,data_source='yahoo',start= yearAgo,end= today)['Adj Close']
        Return = df.pct_change()
        cov_var = Return.cov() *252
        weight = self.portf.loc[:,'Current Value'].divide(self.portfolioValue)
        weight = weight.to_numpy()
        portf_var = np.dot(weight.T,np.dot(cov_var,weight) )
        port_risk = math.sqrt(portf_var)
        portf_return = np.sum(Return.mean()*weight)*252
        port_risk = str(round(port_risk*100,2)) + '%'
        portf_return = str(round(portf_return*100,2)) + '%'
        self.incomeStatrment.loc[0] = [self.portfolioName,portf_return,port_risk,self.PandL]
        print(self.incomeStatrment)
    