from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import Indicator
import portfolio as pf

  

portf1 = pf.Portfolio()
portf1.addStock('2020-01-01','AAPL',130, 1000)
portf1.addStock('2020-02-01','GOOG',200, 500)
portf1.addStock('2020-03-01','NFLX',120, 500)
print(portf1.getPortfolio())




'''plt.style.use("fivethirtyeight")

asset = ['FB','AMZN','AAPL','NFLX','GOOG']
weights = np.array([0.2,0.2,0.2,0.2,0.2])

stockStartDate = "2019-01-01"
today = datetime.today().strftime('%Y-%m-%d')
print(today)

df = pd.DataFrame()

for stock in asset:
    df[stock] = web.DataReader(stock, data_source='yahoo',start=stockStartDate,end= today)['Adj Close']

title = 'Average Moving'

portfolio = df

for stock in portfolio.columns.values:
    plt.plot(df[stock],label=stock)
plt.title(title)
plt.xlabel('Date', fontsize =18)
plt.ylabel('Price(USD)',fontsize=18)
plt.legend()
plt.show()'''