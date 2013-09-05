'''
Created on 2013-8-29

@author: Simon
'''
import  requests
import simplejson as json

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

#return string data in collection,rather than unicode data    
def get_string_data(data):
    js = json.dumps(data)
    return js


if __name__ == "__main__":    
    params = dict(
        op='futures'
    )
    orders = get_orders('https://796.com/apiV2/depth/100.html',params)
    bids = orders[0]
    asks = orders[1]
    print bids
    print get_string_data(bids)
    print asks
    trades = get_trades('https://796.com/apiV2/trade/100.html',params)
    print trades
    print len(trades)
    import datetime
    print datetime.datetime.fromtimestamp(trades[0].get('time')).strftime('%Y-%m-%d %H:%M:%S')
    print datetime.datetime.fromtimestamp(trades[len(trades)-1].get('time')).strftime('%Y-%m-%d %H:%M:%S')
    ticker = get_ticker('https://796.com/apiV2/ticker.html',params)
    print ticker
    print get_string_data(ticker)
