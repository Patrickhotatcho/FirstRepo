import pandas as pd
import portfolio

class portfolioList:
    portfListName = ""
    portfList = {}
    incomeStatement = pd.DataFrame(columns=['Portfolio_Name','Portfolio_Expected_Return','Portfolio_Risk','Profit_and_Loss','Invested_Money','Cash','Current_Portfolio_Return','Profit_Trade','Loss_Trade'])
    def __init__(self,name):
        self.portfListName = name
        self.portfList = {}
        self.incomeStatement = pd.DataFrame(columns=['Portfolio_Name','Portfolio_Expected_Return','Portfolio_Risk','Profit_and_Loss','Invested_Money','Cash','Current_Portfolio_Return','Profit_Trade','Loss_Trade'])
    
    def addPortfolio(self,object):
        self.portfList[object.portfolioName] = object
        print(self.portfList)
        length = len(self.incomeStatement)
        self.incomeStatement.loc[len(self.incomeStatement)] = [object.incomeStatement.loc[0,'Portfolio_Name'],object.incomeStatement.loc[0,'Portfolio_Expected_Return'],object.incomeStatement.loc[0,'Portfolio_Risk'],object.incomeStatement.loc[0,'Profit_and_Loss'],object.incomeStatement.loc[0,'Invested_Money'],object.incomeStatement.loc[0,'Cash'],object.incomeStatement.loc[0,'Current_Portfolio_Return'],object.incomeStatement.loc[0,'Profit_Trade'],object.incomeStatement.loc[0,'Loss_Trade']]
    
        print(self.incomeStatement)



