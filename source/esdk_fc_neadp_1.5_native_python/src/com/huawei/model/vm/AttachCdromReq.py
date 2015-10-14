'''
Created on 2015-3-6

@author: sWX231817
'''

class AttachCdromReq(object):
    '''
    classdocs
    '''
    devicePath = None
    username = None
    password = None
    protocol = None


    def __init__(self, _devicePath=None, _username=None, _password=None, _protocol=None):
        '''
        Constructor
        '''
        self.devicePath = _devicePath
        self.username = _username
        self.password = _password
        self.protocol = _protocol
