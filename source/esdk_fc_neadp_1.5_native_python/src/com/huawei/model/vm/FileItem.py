'''
Created on 2015-3-6

@author: sWX231817
'''

class FileItem(object):
    '''
    classdocs
    '''
    deviceId = None
    path = None
    size = None


    def __init__(self,_deviceId = None,_path = None,_size = None):
        '''
        Constructor
        '''
        self.deviceId = _deviceId
        self.path = _path
        self.size = _size