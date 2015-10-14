'''
Created on 2015-3-6

@author: sWX231817
'''

from com.huawei.model.vm.UsbDevice import UsbDevice

class Usb(object):
    '''
    classdocs
    '''
    controllerType = None
    device = [UsbDevice()]
    usbHostName = None

    def __init__(self, _controllerType=None,_device = None, _usbHostName=None):
        '''
        Constructor
        '''
        self.controllerType = _controllerType
        self.device = _device
        self.usbHostName = _usbHostName
