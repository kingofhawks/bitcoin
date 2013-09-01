'''
Created on 2013-8-29

@author: Simon
'''
import  requests

def get_json(url,params):   
    resp = requests.get(url=url, params=params)
    data = resp.json()
    return data
    
def get_orders(url,params):
    json = get_json(url,params)
    #print json
    data = json.get('return')
    orders = data.get('bids'),data.get('asks')
    #print orders
    return orders

def get_return(url,params):
    json = get_json(url,params)
    #print json
    data = json.get('return')
    return data

def get_trades(url,params):
    return get_return(url,params)

def get_ticker(url,params):
    return get_return(url,params)

    
params = dict(
        op='futures'
    )
orders = get_orders('https://796.com/apiV2/depth/100.html',params)
bids = orders[0]
asks = orders[1]
print bids
print asks

trades = get_trades('https://796.com/apiV2/trade/100.html',params)
print trades
print len(trades)
import datetime
print datetime.datetime.fromtimestamp(trades[0].get('time')).strftime('%Y-%m-%d %H:%M:%S')
print datetime.datetime.fromtimestamp(trades[len(trades)-1].get('time')).strftime('%Y-%m-%d %H:%M:%S')
print get_ticker('https://796.com/apiV2/ticker.html',params)