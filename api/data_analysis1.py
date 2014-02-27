'''
Created on 2013-9-3

@author: Simon
'''
import numpy as np
import pandas as pd
from pandas import *
import random

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,3),index=dates,columns=['TIMESTAMP','PRICE','VOLUME'])
print df
#df.TIMESTAMP = pd.to_datetime(df.TIMESTAMP, unit='s')
#df.set_index('TIMESTAMP', inplace=True)
#print df
rng = pd.date_range('1/1/2000', periods=10000000, freq='10ms')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
df = ts.resample('5Min')
#print df
#print ts
df = ts.resample('5Min', how='ohlc')
print df
#print ts
ts.resample('5Min', how=np.max)
#print ts
