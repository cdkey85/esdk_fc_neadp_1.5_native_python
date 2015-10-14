'''
Created on 2015-3-6

@author: sWX231817
'''

class IpAddress6(object):
    '''
    classdocs
    '''
    ipv6Addr = None
    ipv6Prefix = None


    def __init__(self, _ipv6Addr=None, _ipv6Prefix=None):
        '''
        Constructor
        '''
        self.ipv6Addr = _ipv6Addr
        self.ipv6Prefix = _ipv6Prefix
