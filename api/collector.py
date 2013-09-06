'''
Created on 2013-8-29

@author: Simon
'''
import  requests
import simplejson as json
from api.models import Trade

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

#get accumulated volume of asks or bids
def get_accumulated_volume(orders):
    for i in range(len(orders)):
        order = orders[i]
        previous = 0
        if (i>=1):
            previous = orders[i-1][2] 
        order.append(float(str(order[1]))+float(previous))
    return orders

#save live trades into DB
def save_trades(trades):        
    for data in trades:
        time = int(data['time'])
        if (int(time)>int(get_latest_trade_time())):
            trade = Trade()        
            trade.time = time
            trade.price = float(data['price'])
            trade.amount = float(data['amount'])
            trade.type = data['type']
            trade.save()

#get the latest trade's time        
def get_latest_trade_time():
    trades = Trade.objects.order_by('-time')
    return trades[0].time

if __name__ == "__main__":    
    params = dict(
        op='futures'
    )
    orders = get_orders('https://796.com/apiV2/depth/100.html',params)
    bids = orders[0]
    asks = orders[1]
    print bids
    print get_string_data(get_accumulated_volume(bids))
    print asks
    asks1 = get_string_data(asks)
    print asks1
#    import simplejson as json
#    data = json.loads(asks1)
    print '***************'
#    for i in range(len(asks)):
#        ask = asks[i]
#        previous = 0
#        if (i>=1):
#            previous = asks[i-1][2] 
#        ask.append(float(str(ask[1]))+float(previous))
#
#    print asks
    print get_string_data(get_accumulated_volume(asks))

    trades = get_trades('https://796.com/apiV2/trade/100.html',params)
    print trades
    print len(trades)
    print get_latest_trade_time()
    save_trades(trades)

    import datetime
    print datetime.datetime.fromtimestamp(trades[0].get('time')).strftime('%Y-%m-%d %H:%M:%S')
    print datetime.datetime.fromtimestamp(trades[len(trades)-1].get('time')).strftime('%Y-%m-%d %H:%M:%S')
    ticker = get_ticker('https://796.com/apiV2/ticker.html',params)
    print ticker
    print get_string_data(ticker)
