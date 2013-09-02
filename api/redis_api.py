import redis


def publish(data):
    r = redis.StrictRedis(host='192.168.192.128', port=6379, db=0)
    r.publish('chat', data)
    
params = dict(
        op='futures'
    )
from collector import get_ticker,get_string_data
data = get_ticker('https://796.com/apiV2/ticker.html',params)
#publish({'hello':'redis'})
publish(get_string_data(data))
