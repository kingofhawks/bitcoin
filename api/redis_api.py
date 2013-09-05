import redis


def publish(channel,data):
    r = redis.StrictRedis(host='192.168.192.128', port=6379, db=0)
    r.publish(channel, data)
    
    
    
if __name__ == "__main__":     
    params = dict(
            op='futures'
        )
    
    from collector import get_ticker,get_string_data
    data = get_ticker('https://796.com/apiV2/ticker.html',params)
    publish('chat',get_string_data(data))