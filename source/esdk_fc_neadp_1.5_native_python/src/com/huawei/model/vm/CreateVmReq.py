'''
Created on 2015-3-4

@author: sWX231817
'''
from com.huawei.model.vm.VmConfig import VmConfig 
from com.huawei.model.vm.OsOption import OsOption 
from com.huawei.model.vm.VncAccessInfo import VncAccessInfo 
from com.huawei.model.vm.SecurityGroupSet import SecurityGroupSet 


class CreateVmReq(object):
    '''
    classdocs
    '''
    
    name = None
    description = None
    group = None
    location = None
    isBindingHost = None
    vmConfig = VmConfig() 
    autoBoot = None
    osOptions = OsOption()
    vncAccessInfo = VncAccessInfo()
    occupiedVm = None
    uuid = None
    securityGroupSet = SecurityGroupSet()
    isMultiDiskSpeedup = None

    def __init__(self, _name=None, _description=None, _group=None, _location=None, _isBindingHost=None,
                  _vmConfig=VmConfig() , _autoBoot=None, _osOptions=OsOption(), _vncAccessInfo=None,
                   _occupiedVm=None, _uuid=None, _securityGroupSet=None, _isMultiDiskSpeedup=None):
        '''
        Constructor
        '''
        self.name = _name
        self.description = _description
        self.group = _group
        self.location = _location
        self.isBindingHost = _isBindingHost
        self.vmConfig = _vmConfig
        self.autoBoot = _autoBoot
        self.osOptions = _osOptions
        self.vncAccessInfo = _vncAccessInfo
        self.occupiedVm = _occupiedVm
        self.uuid = _uuid
        self.securityGroupSet = _securityGroupSet
        self.isMultiDiskSpeedup = _isMultiDiskSpeedup
