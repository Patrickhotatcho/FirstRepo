import pandas as pd
from pandas_datareader import data as web
from datetime import datetime, timedelta

class Portfolio:
    noOfStock = 0;
    totalValue = 0;

    df = pd.DataFrame(columns=['Date','Stock','Price','No. of transaction','Value'])

    def __init__(self):
        self.totalValue = 0;
        self.noOfStock = 0;

    def addStock(self, date, stock, price, noOfTransaction):   
        self.noOfStock += 1
        self.totalValue += price*noOfTransaction
        self.df.loc[self.noOfStock-1] = [date,stock,price,noOfTransaction,(price*noOfTransaction)]

    def getPortfolio(self):
        return self.df

    def expectedReturn(self,stock):
        yearAgo = (datetime.today()- timedelta(365)).strftime('%Y-%m-%d')
        today = datetime.today().strftime('%Y-%m-%d')
        try:
            df = web.DataReader(stock, data_source='yahoo',start= yearAgo,end= today)['Adj Close']
        except:
            print('Invalid Input')
        

