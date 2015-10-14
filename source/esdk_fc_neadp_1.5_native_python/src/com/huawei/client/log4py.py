# coding=utf-8
'''
Created on 2015-3-12

@author: sWX231817
'''
import logging

def log_config(fun, url, body, resp):
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='[%y%m%d%H%M%S]',
                    filename='d:\\myapp.log',
                    filemode='a')
        
    logging.debug('[%s] url={%s} body={%s} resp={%s}' % (fun, url, body, resp))
    
