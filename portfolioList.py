import pandas as pd
import portfolio

class portfolioList:
    portfListName = ""
    portfList = {}
    incomeStatement = pd.DataFrame(columns=['Portfolio Name','Portfolio Expected Return(1yr)','Portfolio Risk','Profit and Loss','Invested Money','Cash','Current Portfolio Return','Profit Trade','Loss Trade'])
    def __init__(self,name):
        self.portfListName = name
        self.portfList = {}
        self.incomeStatement = pd.DataFrame(columns=['Portfolio Name','Portfolio Expected Return(1yr)','Portfolio Risk','Profit and Loss','Invested Money','Cash','Current Portfolio Return','Profit Trade','Loss Trade'])
    
    def addPortfolio(self,object):
        self.portfList[object.portfolioName] = object
        print(self.portfList)
        length = len(self.incomeStatement)
        self.incomeStatement.loc[len(self.incomeStatement)] = [object.incomeStatement.loc[0,'Portfolio Name'],object.incomeStatement.loc[0,'Portfolio Expected Return(1yr)'],object.incomeStatement.loc[0,'Portfolio Risk'],object.incomeStatement.loc[0,'Profit and Loss'],object.incomeStatement.loc[0,'Invested Money'],object.incomeStatement.loc[0,'Cash'],object.incomeStatement.loc[0,'Current Portfolio Return'],object.incomeStatement.loc[0,'Profit Trade'],object.incomeStatement.loc[0,'Loss Trade']]
    
        print(self.incomeStatement)



