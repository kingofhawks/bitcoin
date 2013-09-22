'''
Created on 2013-9-7

@author: Simon
'''
import json
from api.models import Ticker,Account,Alert,MtgoxTrade,Futures796Trade,Stockpd796Trade
import logging
logger = logging.getLogger(__name__)

def init_ticker_table():
    with open('markets.json') as data_file:    
        data = json.load(data_file)
    print data
    for d in data:
        market = Ticker()
        market.name = d['market']
        market.ticker = d['ticker']
        market.depth = d['depth']
        market.trade = d['trade']
        market.save()
    
def get_markets():
    return Ticker.objects.order_by('name')

def get_market_by_name(market):
    return Ticker.objects.filter(name=market)

def save_account(account):
    account.save()
    
def get_account(username,password):
    account = Account.objects.filter(username=username,password = password)
    return account

def get_account_by_email(email):
    account = Account.objects.filter(mail=email)
    return account

def get_alert(username,market):
    alert = Alert.objects.filter(username=username,market = market)
    return alert

def update_alerts(username,market,high,low):
    Alert.objects.filter(username=username,market = market).update(high=high,low=low)
    
def get_trades_by_market(market):
    data = []
    logger.debug('begin load trades*****')
    if (market == 'MTgox'):
        #trades = MtgoxTrade.objects.all()[:1000000] test only
        trades = MtgoxTrade.objects.values_list('time','price','amount')
        #trades = MtgoxTrade.objects.values('time','price','amount','type')
    elif (market == '796futures'):
        #trades = Futures796Trade.objects.all()
        trades = Futures796Trade.objects.values('time','price','amount','type')
    elif (market == '796stockpd'):
        #trades = Stockpd796Trade.objects.all()
        trades = Futures796Trade.objects.values('time','price','amount','type')
    
    logger.debug('finish query for trades*****')
    #for trade in trades:
#    for trade in trades.iterator():
#            js = {}
#            js['time']= trade.time
#            js['price']= trade.price
#            js['amount']= trade.amount
#            js['type']= trade.type
#            data.append(js)
            
    for trade in trades.iterator():
        #print trade
        js = {}
        js['time']= trade[0]
        js['price']= trade[1]
        js['amount']= trade[2]
        #js['type']= trade[3]
        data.append(js)
            
#    data = [{'time': trade.time, 'price': trade.price, 'amount': trade.amount, 'type': trade.type}
#        for trade in trades]
    logger.debug('end encode json*****')
#    from django.core import serializers
#
#    data = serializers.serialize("json", 
#                             trades, 
#                             fields=('time','price','amount','type'))

    return data
    #return trades

def get_last30_trades(market):
    data = []
    
    if (market == 'MTgox'):
        trades = MtgoxTrade.objects.order_by('-tid')[:30]
    elif (market == '796futures'):
        trades = Futures796Trade.objects.order_by('-tid')[:30]
    elif (market == '796stockpd'):
        trades = Stockpd796Trade.objects.order_by('-tid')[:30]
    
    for trade in trades:
            js = dict()
            js['time']= trade.time
            js['price']= trade.price
            js['amount']= trade.amount
            js['type']= trade.type
            js['tid']= trade.tid
            data.append(js)
    return data
        
if __name__ == "__main__":     
    #init_ticker_table()
#    print get_markets()
#    from urlparse import urlparse, parse_qsl
#    o = urlparse('https://796.com/apiV2/depth/100.html?op=futures')
#    query_dict = dict(parse_qsl(o.query))
    #d = dict(o.query)
#    print query_dict
#    print get_account('a','b')
#    print get_account_by_email('aa@z.cn')
#    print get_alert('simon','test')
#    update_alerts('simon','test',0,0)
#    print get_market_by_name('796futures')
    print get_trades_by_market('MTgox')
    #print get_last30_trades('MTgox')