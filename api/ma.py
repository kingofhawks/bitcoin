'''
Created on 2013-9-4

@author: Simon
'''
from pandas.io.data import DataReader
import matplotlib.pyplot as plt
import datetime
import pandas as pd

msft = DataReader("MSFT", "yahoo", datetime.datetime(2007, 1, 1),
    datetime.datetime(2012,1,1))
#print msft.to_json()
msft['30_MA_Open'] = pd.stats.moments.rolling_mean(msft['Open'], 30)
print msft['30_MA_Open']
msft['150_MA_Open'] = pd.stats.moments.rolling_mean(msft['Open'], 150)
msft[20:60]