'''
Created on 2013-9-17

@author: Simon
'''
from api.utils import get_query_parameters
from api.collector import get_json
from api.models import MtgoxTrade

def poll_history(url):    
    #resp = requests.get(url=url)
    params = get_query_parameters(url)
    json = get_json(url,params)
    data = json.get('return')
    result = []
    #print data
    for trade in data:
        mtgox = MtgoxTrade()
        mtgox.amount = trade['amount']
        mtgox.time = trade['date']
        mtgox.price = trade['price']
        mtgox.type = trade['trade_type']
        mtgox.save()
        
#        js = dict()
#        js['time']= trade['date']
#        js['price']= trade['price']
#        js['amount']= trade['amount']
#        js['type']= trade['trade_type']
#        result.append(js)
        #print js
    #print result
    last_data = data[len(data)-1]
    #print last_data
    last_tid = last_data.get('tid')
    #print last_tid
    if (long(last_tid)<long(params.get('since'))):
        print 'return now'
        return 
    url = 'https://data.mtgox.com/api/1/BTCusd/trades?since='+last_tid
    #poll_history(url)
    return result
    
if __name__=='__main__':
    url = 'https://data.mtgox.com/api/1/BTCusd/trades?since=1316354111564378'
    print poll_history(url)
    
    