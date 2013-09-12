'''
Created on 2013-9-3

@author: Simon
'''
import numpy as np
import pandas as pd
from pandas import *
from collector import get_string_data,get_trades

#Moving Average
#def MA(df, n):
#    MA = Series(rolling_mean(df['close'], n,min_periods=1), name = 'MA_' + str(n))
#    df = df.join(MA)
#    return df

def MA(df, n,name):
    MA = Series(rolling_mean(df['close'], n,min_periods=1), name = name)
    df = df.join(MA)
    return df

#MACD, MACD Signal and MACD difference
def MACD(df, n_fast, n_slow,span = 9):
    #EMAfast = Series(ewma(df['close'], span = n_fast, min_periods = n_slow - 1))
    #EMAslow = Series(ewma(df['close'], span = n_slow, min_periods = n_slow - 1))
    EMAfast = Series(ewma(df['close'], span = n_fast, min_periods = 1))
    EMAslow = Series(ewma(df['close'], span = n_slow, min_periods = 1))
#    MACD = Series(EMAfast - EMAslow, name = 'MACD_' + str(n_fast) + '_' + str(n_slow))
#    MACDsign = Series(ewma(MACD, span, min_periods = 1), name = 'MACDsign_' + str(n_fast) + '_' + str(n_slow))
#    MACDdiff = Series(MACD - MACDsign, name = 'MACDdiff_' + str(n_fast) + '_' + str(n_slow))
    MACD = Series(EMAfast - EMAslow, name = 'MACD_12_26')
    MACDsign = Series(ewma(MACD, span, min_periods = 1), name = 'MACDsign_12_26')
    MACDdiff = Series(MACD - MACDsign, name = 'MACDdiff_12_26')
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    return df

#Relative Strength Index
def RSI(df, n):
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= df.index[-1]:
        UpMove = df.get_value(i + 1, 'High') - df.get_value(i, 'High')
        DoMove = df.get_value(i, 'Low') - df.get_value(i + 1, 'Low')
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else: UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else: DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = Series(UpI)
    DoI = Series(DoI)
    PosDI = Series(ewma(UpI, span = n, min_periods = n - 1))
    NegDI = Series(ewma(DoI, span = n, min_periods = n - 1))
    RSI = Series(PosDI / (PosDI + NegDI), name = 'RSI_' + str(n))
    df = df.join(RSI)
    return df


if __name__ == '__main__':
    d = {'TIMESTAMP' : Series([1294311545, 1294317813, 1294318449]),
          'PRICE' : Series([24990, 25499, 25499]),
          'VOLUME' : Series([1500000000, 5000000000, 100000000])}
    df = DataFrame(d)
    print df
    df.TIMESTAMP = pd.to_datetime(df.TIMESTAMP, unit='s')
    df.set_index('TIMESTAMP', inplace=True)
    print df
    test = df['VOLUME'].resample('H', how='ohlc')
    print test
    #print df
    test2= df['PRICE'].resample('H', how='ohlc')
    print test2
    
    #load from JSON data
    print 'load json data************************'
    #data = [{u'price': u'129.13', u'type': u'sell', u'amount': u'40', u'time': 1378343428}, {u'price': u'129.11', u'type': u'sell', u'amount': u'9', u'time': 1378343368}, {u'price': u'129.11', u'type': u'buy', u'amount': u'7.88', u'time': 1378343347}, {u'price': u'129.11', u'type': u'sell', u'amount': u'69.22', u'time': 1378343342}, {u'price': u'129.11', u'type': u'sell', u'amount': u'18.84', u'time': 1378343340}, {u'price': u'129.11', u'type': u'sell', u'amount': u'82', u'time': 1378343293}, {u'price': u'129.13', u'type': u'buy', u'amount': u'6.38', u'time': 1378343240}, {u'price': u'129.13', u'type': u'sell', u'amount': u'8', u'time': 1378343228}, {u'price': u'130.00', u'type': u'buy', u'amount': u'8.92', u'time': 1378343211}, {u'price': u'129.15', u'type': u'buy', u'amount': u'7.08', u'time': 1378343211}, {u'price': u'129.15', u'type': u'sell', u'amount': u'9.92', u'time': 1378343210}, {u'price': u'129.15', u'type': u'buy', u'amount': u'9.92', u'time': 1378343178}, {u'price': u'129.11', u'type': u'sell', u'amount': u'4', u'time': 1378343145}, {u'price': u'129.15', u'type': u'sell', u'amount': u'38.9', u'time': 1378343132}, {u'price': u'129.10', u'type': u'sell', u'amount': u'4', u'time': 1378343107}, {u'price': u'129.11', u'type': u'sell', u'amount': u'4', u'time': 1378343045}, {u'price': u'129.02', u'type': u'sell', u'amount': u'56', u'time': 1378342988}, {u'price': u'129.10', u'type': u'sell', u'amount': u'12', u'time': 1378342988}, {u'price': u'129.30', u'type': u'sell', u'amount': u'20', u'time': 1378342988}, {u'price': u'129.10', u'type': u'sell', u'amount': u'8', u'time': 1378342986}, {u'price': u'130.00', u'type': u'buy', u'amount': u'8', u'time': 1378342967}, {u'price': u'130.00', u'type': u'sell', u'amount': u'105.84', u'time': 1378342908}, {u'price': u'130.01', u'type': u'sell', u'amount': u'81.8', u'time': 1378342908}, {u'price': u'130.05', u'type': u'sell', u'amount': u'5.14', u'time': 1378342908}, {u'price': u'130.50', u'type': u'sell', u'amount': u'7.22', u'time': 1378342908}, {u'price': u'130.05', u'type': u'sell', u'amount': u'34.86', u'time': 1378342888}, {u'price': u'130.00', u'type': u'sell', u'amount': u'112', u'time': 1378342883}, {u'price': u'130.00', u'type': u'sell', u'amount': u'60', u'time': 1378342868}, {u'price': u'130.00', u'type': u'sell', u'amount': u'80', u'time': 1378342858}, {u'price': u'130.00', u'type': u'sell', u'amount': u'40', u'time': 1378342852}, {u'price': u'130.00', u'type': u'sell', u'amount': u'8', u'time': 1378342771}, {u'price': u'130.00', u'type': u'sell', u'amount': u'28', u'time': 1378342768}, {u'price': u'130.00', u'type': u'buy', u'amount': u'3.44', u'time': 1378342762}, {u'price': u'130.00', u'type': u'buy', u'amount': u'372.78', u'time': 1378342758}, {u'price': u'130.00', u'type': u'buy', u'amount': u'40', u'time': 1378342752}, {u'price': u'130.00', u'type': u'sell', u'amount': u'577.78', u'time': 1378342748}, {u'price': u'130.00', u'type': u'sell', u'amount': u'1000', u'time': 1378342745}, {u'price': u'130.00', u'type': u'sell', u'amount': u'104', u'time': 1378342744}, {u'price': u'130.00', u'type': u'sell', u'amount': u'291', u'time': 1378342740}, {u'price': u'130.00', u'type': u'sell', u'amount': u'717.3', u'time': 1378342732}, {u'price': u'130.01', u'type': u'sell', u'amount': u'170', u'time': 1378342732}, {u'price': u'130.02', u'type': u'sell', u'amount': u'490', u'time': 1378342732}, {u'price': u'130.08', u'type': u'sell', u'amount': u'86.2', u'time': 1378342732}, {u'price': u'130.08', u'type': u'sell', u'amount': u'14', u'time': 1378342722}, {u'price': u'130.08', u'type': u'sell', u'amount': u'40', u'time': 1378342716}, {u'price': u'130.08', u'type': u'sell', u'amount': u'61.8', u'time': 1378342711}, {u'price': u'130.09', u'type': u'sell', u'amount': u'20.04', u'time': 1378342711}, {u'price': u'130.10', u'type': u'sell', u'amount': u'3.2', u'time': 1378342711}, {u'price': u'130.20', u'type': u'sell', u'amount': u'3.4', u'time': 1378342711}, {u'price': u'130.25', u'type': u'sell', u'amount': u'26', u'time': 1378342694}, {u'price': u'130.50', u'type': u'sell', u'amount': u'3.56', u'time': 1378342685}, {u'price': u'130.50', u'type': u'sell', u'amount': u'120', u'time': 1378342680}, {u'price': u'130.50', u'type': u'sell', u'amount': u'20', u'time': 1378342673}, {u'price': u'130.50', u'type': u'sell', u'amount': u'30.38', u'time': 1378342663}, {u'price': u'130.50', u'type': u'sell', u'amount': u'18.06', u'time': 1378342654}, {u'price': u'131.01', u'type': u'sell', u'amount': u'16.24', u'time': 1378342586}, {u'price': u'132.00', u'type': u'sell', u'amount': u'40', u'time': 1378342556}, {u'price': u'132.10', u'type': u'sell', u'amount': u'40', u'time': 1378342556}, {u'price': u'132.20', u'type': u'sell', u'amount': u'40', u'time': 1378342552}, {u'price': u'132.25', u'type': u'sell', u'amount': u'79.26', u'time': 1378342513}, {u'price': u'132.30', u'type': u'sell', u'amount': u'40', u'time': 1378342513}, {u'price': u'132.40', u'type': u'sell', u'amount': u'40', u'time': 1378342513}, {u'price': u'132.50', u'type': u'sell', u'amount': u'290.54', u'time': 1378342513}, {u'price': u'132.50', u'type': u'sell', u'amount': u'166.76', u'time': 1378342507}, {u'price': u'132.60', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'132.70', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'132.80', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'132.90', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'133.00', u'type': u'sell', u'amount': u'40', u'time': 1378342507}, {u'price': u'133.10', u'type': u'sell', u'amount': u'33.24', u'time': 1378342507}, {u'price': u'133.10', u'type': u'sell', u'amount': u'6.76', u'time': 1378342494}, {u'price': u'133.20', u'type': u'sell', u'amount': u'40', u'time': 1378342494}, {u'price': u'133.30', u'type': u'sell', u'amount': u'40', u'time': 1378342494}, {u'price': u'133.33', u'type': u'sell', u'amount': u'3.24', u'time': 1378342494}, {u'price': u'133.40', u'type': u'sell', u'amount': u'40', u'time': 1378342463}, {u'price': u'133.50', u'type': u'sell', u'amount': u'240', u'time': 1378342463}, {u'price': u'133.51', u'type': u'sell', u'amount': u'120', u'time': 1378342463}, {u'price': u'133.60', u'type': u'sell', u'amount': u'40', u'time': 1378342457}, {u'price': u'133.70', u'type': u'sell', u'amount': u'24', u'time': 1378342420}, {u'price': u'133.70', u'type': u'sell', u'amount': u'16', u'time': 1378342406}, {u'price': u'133.75', u'type': u'sell', u'amount': u'2', u'time': 1378342381}, {u'price': u'133.80', u'type': u'sell', u'amount': u'1.02', u'time': 1378342273}, {u'price': u'133.80', u'type': u'sell', u'amount': u'4', u'time': 1378342266}, {u'price': u'133.80', u'type': u'sell', u'amount': u'100', u'time': 1378342263}, {u'price': u'133.80', u'type': u'sell', u'amount': u'80', u'time': 1378342253}, {u'price': u'133.80', u'type': u'sell', u'amount': u'6.98', u'time': 1378342234}, {u'price': u'133.80', u'type': u'sell', u'amount': u'48', u'time': 1378342226}, {u'price': u'133.90', u'type': u'sell', u'amount': u'40', u'time': 1378342218}, {u'price': u'134.00', u'type': u'sell', u'amount': u'3.1', u'time': 1378342202}, {u'price': u'134.00', u'type': u'sell', u'amount': u'65', u'time': 1378342200}, {u'price': u'134.00', u'type': u'sell', u'amount': u'3.62', u'time': 1378342194}, {u'price': u'134.00', u'type': u'sell', u'amount': u'24', u'time': 1378342193}, {u'price': u'134.00', u'type': u'sell', u'amount': u'1000', u'time': 1378342192}, {u'price': u'134.00', u'type': u'sell', u'amount': u'2', u'time': 1378342189}, {u'price': u'134.00', u'type': u'sell', u'amount': u'8', u'time': 1378342189}, {u'price': u'134.00', u'type': u'sell', u'amount': u'40.48', u'time': 1378342161}, {u'price': u'134.01', u'type': u'sell', u'amount': u'2.98', u'time': 1378342156}, {u'price': u'134.01', u'type': u'sell', u'amount': u'120', u'time': 1378342151}, {u'price': u'134.10', u'type': u'buy', u'amount': u'42', u'time': 1378342126}, {u'price': u'134.10', u'type': u'sell', u'amount': u'5.58', u'time': 1378342125}]
    params = dict(
            op='futures'
        )
    data = get_trades('https://796.com/apiV2/trade/100.html',params)
    print data
    print len(data)    
    
    d = pd.read_json(get_string_data(data))
    d.time = pd.to_datetime(d.time, unit='s')
    d.set_index('time', inplace=True)
    #print d.to_json(orient='records')
    
    print 'price***************'
    period = '15Min'
    volume = d['amount'].resample(period, how='sum') #maybe how should be "sum"?
    print volume
    print volume.reset_index().to_json(date_format='iso', orient='records')
    print type(volume)
    
    price = d['price'].resample(period, how='ohlc')
    print price
    print type(price)
    
    #join OHLC and volume
    s = Series(volume,name='amount')
    a = price.join(s)
    print a
    
    print '****************OHLC with volume***************'
    js = a.reset_index().to_json(date_format='iso', orient='records')
    print js
    #price.join(volume)
    #merged = merge(price, volume,on='time')
    #print 'joined***************'
    #print merged.to_json(date_format='iso', orient='records')
    
    print 'ma***************'
    ma = MA(price,7,'MA_7')
    print ma.to_json(date_format='iso', orient='records')
    
    print 'MACD***************'
    macd = MACD(price,12,26,9)
    print macd.to_json(date_format='iso', orient='records')
    
    js = price.to_json(date_format='iso', orient='records')
    #print js
    price = d['price'].resample(period, how='ohlc').reset_index()
    print price
    js = price.to_json(date_format='iso', orient='records')
    print js