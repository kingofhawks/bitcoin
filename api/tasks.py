'''
Created on 2013-9-2

@author: Simon
'''
from collector import get_ticker,get_trades,get_orders,get_string_data,get_accumulated_volume,save_trades
from redis_api import publish
from celery import task

@task()
def polling_market_data():
    params = dict(
        op='futures'
    )
    #live price
    data = get_ticker('https://796.com/apiV2/ticker.html',params)
    publish('chat',get_string_data(data))
    
    orders = get_orders('https://796.com/apiV2/depth/100.html',params)
    bids = orders[0]
    asks = orders[1]

    #live asks
    publish('asks',get_string_data(get_accumulated_volume(asks)))
    
    #live bids
    publish('bids',get_string_data(get_accumulated_volume(bids)))
    
    #live trades
    trades = get_trades('https://796.com/apiV2/trade/100.html?op=futures',params)
    publish('trades',get_string_data(trades))
    
    #save trades to DB
    save_trades(trades)