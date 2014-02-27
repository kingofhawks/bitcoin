'''
Created on 2013-8-29

@author: Simon
'''
import  requests
import simplejson as json
from api.models import Trade,MtgoxTrade,Futures796Trade,Stockpd796Trade
from api.utils import get_query_parameters
from api.history import poll_history

def get_json(url,params):   
    if params is None:
        resp = requests.get(url=url)
        #print resp.text
        data = resp.json()    
        return data
    else:
        resp = requests.get(url=url, params=params)
        #print resp.text
        data = resp.json()    
        return data

def get_json2(url):   
    resp = requests.get(url=url)
    #print resp.text
    data = resp.json()    
    return data
    
def get_orders(url,params):
    json = get_json(url,params)
    #print json
    data = json.get('return')
    orders = data.get('bids'),data.get('asks')
    #print orders
    return orders

def get_orders2(url):
    params = get_query_parameters(url)
    json = get_json(url,params)
    #print json
    data = json.get('return')
    if (url.find('mtgox') != -1):
        bids = []
        bidsJson = data.get('bids')
        for bid in bidsJson:
            b = []
            b.append(bid.get('price'))
            b.append(bid.get('amount'))
            bids.append(b)
            
        asks = []
        asksJson = data.get('asks')
        for ask in asksJson:
            b = []
            b.append(ask.get('price'))
            b.append(ask.get('amount'))
            asks.append(b)
            
        return bids,asks
    else:
        orders = data.get('bids'),data.get('asks')
        #print orders
        return orders

def get_return(url,params):
    json = get_json(url,params)
    #print json
    data = json.get('return')
    return data

def get_trades(url,params):
    if (url.find('mtgox') != -1):
#        return get_json(url,params)
        size = 700 #default show 30 trades
        data =  poll_history(url,False)
        length = len(data)
        if (length >=30):
            offset = length-size
        else:
            offset = 0
        result = data[offset:length]
        #save last tid
        last_tid =  data[length-1]['tid']
        print last_tid
        
        #Sort by tid
        return sorted(result, key=lambda trade: trade['tid'],reverse=True)        
        #return result
    else:
        return get_return(url,params)

def get_ticker(url,params):
    result = get_return(url,params)
    if (url.find('mtgox') != -1):
        print result
        #return get_json(url,params)
    return result

def get_ticker2(url):
    params = get_query_parameters(url)
    result = get_return(url,params)
    if (url.find('mtgox') != -1):
        high = result['high']['value']
        low = result['low']['value']
        last = result['last']['value']
        vol = result['vol']['value']
        sell = result['sell']['value']
        buy = result['buy']['value']
        result['high'] = high
        result['low'] = low
        result['last'] = last
        result['vol'] = vol
        result['sell'] = sell
        result['buy'] = buy
        #print sell
        #print result
        #return get_json(url,params)
    return result

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
        print str(order[1])
        print previous
        amount = float(str(order[1]))+float(previous)
        order.append("{0:.2f}".format(amount))
    return orders

#save live trades into DB
def save_trades(market,trades):    
    last_update = get_latest_trade_time(market) 
    print last_update
       
    for data in trades:
        if (market == 'MTgox'):
            time = int(data['time'])
            trade = MtgoxTrade()
            trade.tid = data['tid']
            #return 
        elif (market == '796futures'):  
            time = int(data['time'])
            trade = Futures796Trade()
        elif (market == '796stockpd'):
            time = int(data['time'])
            trade = Stockpd796Trade()          
        
        
        if (int(time)>int(last_update)):
            trade.time = time
            trade.price = float(data['price'])
            trade.amount = float(data['amount'])
            trade.type = data['type']
            trade.save()
            
#save live price into DB
def save_live_price(live_price):
    from api.models import Ticker
    ticker = Ticker.objects.get(name=live_price['market'])
    ticker.last = live_price['last']
    ticker.high = live_price['high']
    ticker.low = live_price['low']
    ticker.vol = live_price['vol']
    ticker.sell = live_price['sell']
    ticker.buy = live_price['buy']
    ticker.save()        


#get the latest trade's time        
def get_latest_trade_time(market):
    if (market == 'MTgox'):
        trades = MtgoxTrade.objects.order_by('-tid')                   
    elif (market == '796futures'):  
        trades = Futures796Trade.objects.order_by('-time')                
    elif (market == '796stockpd'):
        trades = Stockpd796Trade.objects.order_by('-time')                

    if (len(trades)>=1):
        if (market == 'MTgox'):
            return trades[0].tid
        else:
            return trades[0].time
    else:
        return 0

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
    print get_string_data(get_accumulated_volume(asks))

    trades = get_trades('https://796.com/apiV2/trade/100.html',params)
    print trades
    
    trades = get_trades('https://data.mtgox.com/api/1/BTCUSD/trades?raw',params)
    print trades

    print get_latest_trade_time('MTgox')
    #save_trades(trades)

    import datetime
    print datetime.datetime.fromtimestamp(trades[0].get('time')).strftime('%Y-%m-%d %H:%M:%S')
    print datetime.datetime.fromtimestamp(trades[len(trades)-1].get('time')).strftime('%Y-%m-%d %H:%M:%S')
#    resp = requests.get('http://data.mtgox.com/api/1/BTCUSD/ticker')
#    print resp.text
    ticker = get_ticker2('http://data.mtgox.com/api/1/BTCUSD/ticker') 
    print ticker     
    
    ticker = get_ticker2('https://796.com/apiV2/ticker.html?op=futures') 
    print ticker  
#    print get_string_data(ticker)

    orders = get_orders2('http://data.mtgox.com/api/1/BTCUSD/depth/fetch')
    bids = orders[0]
    asks = orders[1]
    print bids
    print get_string_data(get_accumulated_volume(bids))
    print asks
    asks1 = get_string_data(asks)
    print asks1
