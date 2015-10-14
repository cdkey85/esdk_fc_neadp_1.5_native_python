'''
Created on 2015-3-7

@author: sWX231817
'''

from com.huawei.model.vm.VmConfig import VmConfig
from com.huawei.model.vm.OsOption import OsOption
from com.huawei.model.vm.FileItem import FileItem
from com.huawei.model.vm.VmCustomization import VmCustomization
from com.huawei.model.vm.VncAccessInfo import VncAccessInfo
from com.huawei.model.vm.SecurityGroupSet import SecurityGroupSet

class ImportVmTempReq(object):
    '''
    classdocs
    '''

    name = None
    description = None
    group = None
    location = None
    vmConfig = VmConfig()
    osOptions = OsOption()
    fileItems = [FileItem()]
    url = None
    protocol = None
    username = None
    password = None
    autoBoot = None
    publickey = None
    vmCustomization = VmCustomization()
    vncAccessInfo = VncAccessInfo()
    isTemplate = None
    vmId = None
    uuid = None
    isBindingHost = None
    securityGroupSet = SecurityGroupSet()
    recover = None
    isMultiDiskSpeedup = None


    def __init__(self, _name=None, _description=None, _group=None, _location=None, _vmConfig=None, _osOptions=None, _fileItems=None,
                  _url=None, _protocol=None, _username=None, _password=None, _autoBoot=None, _publickey=None, _vmCustomization=None,
                   _vncAccessInfo=None, _isTemplate=None, _vmId=None, _uuid=None, _isBindingHost=None, _securityGroupSet=None,
                    _recover=None, _isMultiDiskSpeedup=None):
        '''
        Constructor
        '''
        self.name = _name
        self.description = _description
        self.group = _group
        self.location = _location
        self.vmConfig = _vmConfig
        self.osOptions = _osOptions
        self.fileItems = _fileItems
        self.url = _url
        self.protocol = _protocol
        self.username = _username
        self.password = _password
        self.autoBoot = _autoBoot
        self.publickey = _publickey
        self.vmCustomization = _vmCustomization
        self.vncAccessInfo = _vncAccessInfo
        self.isTemplate = _isTemplate
        self.vmId = _vmId
        self.uuid = _uuid
        self.isBindingHost = _isBindingHost
        self.securityGroupSet = _securityGroupSet
        self.recover = _recover
        self.isMultiDiskSpeedup = _isMultiDiskSpeedup
