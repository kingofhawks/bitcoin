'''
Created on 2013-9-2

@author: Simon
'''
from collector import get_ticker,get_string_data
from redis_api import publish
from celery import task

@task()
def polling_market_data():
    params = dict(
        op='futures'
    )
    data = get_ticker('https://796.com/apiV2/ticker.html',params)
    #publish({'hello':'redis'})
    publish(get_string_data(data))