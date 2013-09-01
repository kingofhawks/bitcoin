import redis


def publish():
    r = redis.StrictRedis(host='192.168.192.128', port=6379, db=0)
    r.publish('chat', {'hello':'redis'})
    
publish()
