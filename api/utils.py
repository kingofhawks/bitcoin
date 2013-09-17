'''
Created on 2013-9-16

@author: Simon
'''
from urlparse import urlparse, parse_qsl
def get_query_parameters(url):        
    u = urlparse(url)
    query_dict = dict(parse_qsl(u.query))
    return query_dict