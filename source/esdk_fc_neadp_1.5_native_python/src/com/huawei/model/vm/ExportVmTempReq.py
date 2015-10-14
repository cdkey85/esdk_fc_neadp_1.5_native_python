'''
Created on 2015-3-7

@author: sWX231817
'''

from com.huawei.model.vm.VmConfig import VmConfig

class ExportVmTempReq(object):
    '''
    classdocs
    '''
    name = None
    format = None
    url = None
    protocol = None
    username = None
    password = None
    isOverwrite = None
    vmConfig = VmConfig()


    def __init__(self, _name=None, _format=None, _url=None, _protocol=None, _username=None, _password=None, _isOverwrite=None,
                  _vmConfig=None):
        '''
        Constructor
        '''
        self.name = _name
        self.format = _format
        self.url = _url
        self.protocol = _protocol
        self.username = _username
        self.password = _password
        self.isOverwrite = _isOverwrite
        self.vmConfig = _vmConfig
