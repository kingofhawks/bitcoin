'''
Created on 2013-9-16

@author: Simon
'''
from urlparse import urlparse, parse_qsl
import  requests

def get_query_parameters(url):        
    u = urlparse(url)
    query_dict = dict(parse_qsl(u.query))
    return query_dict

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