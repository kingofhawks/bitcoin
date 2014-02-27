'''
Created on 2013-9-17

@author: Simon
'''
from api.utils import get_query_parameters
from api.utils import get_json
from api.models import MtgoxTrade

def poll_history(url,save):    
    #resp = requests.get(url=url)
    params = get_query_parameters(url)
    json = get_json(url,params)
    #print json
    if ('return' in json):
        data = json.get('return')
    else:
        data = json
    result = []
    #print data
    for trade in data:
        if save:
            mtgox = MtgoxTrade()
            mtgox.amount = trade['amount']
            mtgox.time = trade['date']
            mtgox.price = trade['price']
            mtgox.type = trade['trade_type']
            mtgox.tid = trade['tid']
            #print mtgox.tid
            mtgox.save()
        else:     
            js = dict()
            js['time']= trade['date']
            js['price']= trade['price']
            js['amount']= trade['amount']
            js['type']= trade['trade_type']
            js['tid']= trade['tid']
            result.append(js)
        #print js
    #print result
    length = len(data)-1
    if (length >=1):
        last_data = data[length]
    else:
        return result
    #print last_data
    last_tid = last_data.get('tid')
    #print last_tid
    since = params.get('since')
    if (since is not None and long(last_tid)<long(since)):
        print 'Finish polling mgtox history data'
        return 
    url = 'https://data.mtgox.com/api/1/BTCusd/trades?since='+last_tid
    if save:
        poll_history(url,save)
        return
    else:
        result.extend(poll_history(url,save))
        return result
    
if __name__=='__main__':
    url = 'https://data.mtgox.com/api/1/BTCusd/trades?since=1316354111564378'
    #poll_history(url,True)
    url = 'https://data.mtgox.com/api/1/BTCusd/trades?raw'
    result= poll_history(url,False)
    length = len(result)
    last_tid =  result[0]['tid']
    print last_tid
    print len(result)
    print result[length-30:length-1]
    import redis
    r = redis.StrictRedis(host='192.168.192.128', port=6379, db=0)
    r.set(last_tid,result[length-30:length-1])
    print r.get(last_tid)
    #print poll_history(url,True)
    
    