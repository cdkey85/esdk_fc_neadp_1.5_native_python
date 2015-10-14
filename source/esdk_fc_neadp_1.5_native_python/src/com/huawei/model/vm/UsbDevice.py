'''
Created on 2015-3-6

@author: sWX231817
'''

class UsbDevice(object):
    '''
    classdocs
    '''
    usbUrn = None

    def __init__(self, _usbUrn=None):
        '''
        Constructor
        '''
        self.usbUrn = _usbUrn
