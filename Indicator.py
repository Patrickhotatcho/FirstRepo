from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from pandas_datareader import data as web
import pandas as pd
import statistics as st

class MovingAverage:

    
    def Price_MA(start,stock,MAday):
        today = datetime.today().strftime('%Y-%m-%d')
        df = pd.DataFrame()
        df2 = pd.DataFrame(columns=['Date','MA'])
        try:
            df = web.DataReader(stock, data_source='yahoo',start= start ,end= today)['Adj Close']
        except:
            print("Invalid Input")
        df = df.reset_index()
        sumOfPrice = 0
        for i in range(len(df['Adj Close'])):
            if(i>MAday):
                for j in range(MAday):
                    sumOfPrice = sumOfPrice + df['Adj Close'][i-j]
                MA = sumOfPrice/MAday
                df2.loc[i-MAday-1] = [df['Date'][i],MA]
                sumOfPrice = 0
        return df2
    
    def Volatility_MA(start,stock,MAday):
        today = datetime.today().strftime('%Y-%m-%d')
        df = pd.DataFrame()
        df2 = pd.DataFrame(columns=['Date','MA'])
        try:
            df = web.DataReader(stock, data_source='yahoo',start= start ,end= today)['Adj Close']
        except:
            print("Invalid Input")
        df = df.pct_change()
        df = df.reset_index()
        for i in range(len(df['Adj Close'])):
            list = []
            if(i>MAday):
                for j in range(MAday):
                    list.append(df['Adj Close'][i-j])
                MA = st.pstdev(list)
                df2.loc[i-MAday-1] = [df['Date'][i],MA]
        return df2
    

    def plotChart(name,title,df,color):
        plt.style.use("fivethirtyeight")
        plt.plot(df['Date'],df['MA'],color)
        plt.title(title)
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Price(USD)',fontsize=18)
        plt.legend(name)

    def combinetTwo(df1,df2):
        plt.legend(df1,df2);


    def combinedChart(title,day1,df1,day2,df2,day3,df3):
        plt.style.use("fivethirtyeight")

        days = min(df1['MA'].count(),df2['MA'].count(),df3['MA'].count())
        plt.plot(df1['Date'].tail(days),df1['MA'].tail(days),'b--',label=(str(day1)+"MA"))
        plt.plot(df1['Date'].tail(days),df2['MA'].tail(days),'r--',label=(str(day2)+"MA"))
        plt.plot(df1['Date'].tail(days),df3['MA'].tail(days),'g--',label=(str(day3)+"MA"))
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Price(USD)',fontsize=18)
        plt.legend()
        plt.show()

                