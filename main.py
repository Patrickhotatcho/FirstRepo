from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import Indicator
import portfolio as pf

  

portf1 = pf.Portfolio("Pat",100000000)
portf1.buyStock('2020-01-01','AAPL',130, 1000)
portf1.buyStock('2020-02-01','GOOG',200, 500)
portf1.buyStock('2020-03-01','NFLX',120, 500)
portf1.buyStock('2020-03-01','NFLX',110, 500)
portf1.buyStock('2020-03-01','NFLX',160, 500)
portf1.sellStock('2020-03-01','AAPL',150,200)
portf1.sellStock('2020-03-01','AAPL',150,800)
print(portf1.getPortfolio())


