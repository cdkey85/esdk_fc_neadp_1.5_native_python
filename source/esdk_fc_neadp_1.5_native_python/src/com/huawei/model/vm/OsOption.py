'''
Created on 2015-3-4

@author: sWX231817
'''

class OsOption(object):
    '''
    classdocs
    '''


    osType = None
    
    osVersion = None
    
    guestOSName = None
    
    hostname = None
    
    password = None

    def __init__(self, _osType=None, _osVersion=None, _guestOSName=None, _hostname=None, _password=None):
        '''
        Constructor
        '''
        
        self.osType = _osType
        self.osVersion = _osVersion
        self.guestOSName = _guestOSName
        self.hostname = _hostname
        self.password = _password
