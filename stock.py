from pandas_datareader import data as web
import pandas as pd
from datetime import datetime, timedelta

class stockDetail:
    df = pd.DataFrame()
    def getStockData(stock,startFrom,endAt):
        startFrom = (datetime.today()- timedelta(startFrom)).strftime('%Y-%m-%d')
        try:
            df = web.DataReader(stock, data_source='yahoo',start= startFrom,end= endAt)['Adj Close']
        except:
            print('Invalid Input')
        return df

    def getStockLatest(stock):
        today = datetime.today().strftime('%Y-%m-%d')
        try:
            df = web.DataReader(stock, data_source='yahoo',start= today,end= today)['Adj Close']
        except:
            print('Invalid Input')
        return float(df)