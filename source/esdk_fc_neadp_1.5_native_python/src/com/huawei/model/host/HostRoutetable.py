'''
Created on 2015-3-7

@author: lWX232078
'''

class HostRoutetable(object):
    '''
    classdocs
    '''
    destination = None
    gateway = None
    maskPrefix = None
    dev = None


    def __init__(self, _destination = None,_gateway = None,_maskPrefix = None,_dev = None):
        '''
        Constructor
        '''
        self.destination = _destination
        self.gateway = _gateway
        self.maskPrefix = _maskPrefix
        self.dev = _dev