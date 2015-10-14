'''
Created on 2015-3-4

@author: sWX231817
'''

class VncAccessInfo(object):
    '''
    classdocs
    '''
    
    hostIp = None
    vncPort = None
    vncPassword = None
    vncOldPassword = None



    def __init__(self, _hostIp=None, _vncPort=None, _vncPassword=None, _vncOldPassword=None):
        '''
        Constructor
        '''
        self.hostIp = _hostIp
        self.vncPort = _vncPort
        self.vncPassword = _vncPassword
        self.vncOldPassword = _vncOldPassword
