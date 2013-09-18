'''
Created on 2013-9-2

@author: Simon
'''
from collector import get_ticker,get_ticker2,get_trades,get_orders,get_orders2,get_string_data,get_accumulated_volume,save_trades,save_live_price
from redis_api import publish
from celery import task
from dao import get_markets
from urlparse import urlparse, parse_qsl

#parse query parameters from URL
def get_query_parameters(url):        
    u = urlparse(url)
    query_dict = dict(parse_qsl(u.query))
    return query_dict
    
def polling(market):
    name = market.name
    ticker = market.ticker
    depth = market.depth
    trade = market.trade
    print '%s,%s,%s,%s' % (name,ticker,depth,trade)
    
    #live price
    live_price = get_ticker2(ticker)
    live_price['market'] = name
    publish('chat',get_string_data(live_price))
    
    #save live price
    save_live_price(live_price)
    
    orders = get_orders2(depth)
    bids = orders[0]
    asks = orders[1]
    #print asks

    #live asks
    live_asks = get_string_data({"market":name,"data":get_string_data(get_accumulated_volume(asks))})
    #print live_asks
    publish('asks',live_asks)
    
    #live bids
    live_bids = get_string_data({"market":name,"data":get_string_data(get_accumulated_volume(bids))})
    publish('bids',live_bids)
    
    #live trades
    trades = get_trades(trade,get_query_parameters(trade))
    print trades
    #publish('trades',get_string_data(trades))
    live_trades = get_string_data({"market":name,"data":get_string_data(trades)})
    #print live_trades
    publish('trades',live_trades)
    
    #save trades to DB
    save_trades(name,trades)
    
    
@task()
def polling_market_data():
    markets = get_markets()
    for market in markets:
        polling(market)
        
if __name__ == '__main__':
    polling_market_data()