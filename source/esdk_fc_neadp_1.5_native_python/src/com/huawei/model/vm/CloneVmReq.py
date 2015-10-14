'''
Created on 2015-3-7

@author: sWX231817
'''
from com.huawei.model.vm.VmConfig import VmConfig 
from com.huawei.model.vm.OsOption import OsOption 
from com.huawei.model.vm.VncAccessInfo import VncAccessInfo 
from com.huawei.model.vm.SecurityGroupSet import SecurityGroupSet 
from com.huawei.model.vm.VmCustomization import VmCustomization 

class CloneVmReq(object):
    '''
    classdocs
    '''
    name = None
    description = None
    group = None
    location = None
    isBindingHost = None
    vmConfig = VmConfig()
    osOptions = OsOption()
    isTemplate = None
    autoBoot = None
    isLinkClone = None
    regionInfo = None
    vmCustomization = VmCustomization()
    publickey = None
    vmData = None
    fileName = None
    vncAccessInfo = VncAccessInfo()
    fileMode = None
    drDrillOption = None
    uuid = None
    isMultiDiskSpeedup = None
    fileNames = [None]
    vmDatas = [None]

    def __init__(self, _name=None, _description=None, _group=None, _location=None, _isBindingHost=None, _vmConfig=None, _osOptions=None,
                  _isTemplate=None, _autoBoot=None, _isLinkClone=None, _regionInfo=None, _vmCustomization=None, _publickey=None,
                   _vmData=None, _fileName=None, _vncAccessInfo=None, _fileMode=None, _drDrillOption=None, _uuid=None,
                    _isMultiDiskSpeedup=None, _fileNames=None, _vmDatas=None):
        '''
        Constructor
        '''
        self.name = _name
        self.description = _description
        self.group = _group
        self.location = _location
        self.isBindingHost = _isBindingHost
        self.vmConfig = _vmConfig
        self.osOptions = _osOptions
        self.isTemplate = _isTemplate
        self.autoBoot = _autoBoot
        self.isLinkClone = _isLinkClone
        self.regionInfo = _regionInfo
        self.vmCustomization = _vmCustomization
        self.publickey = _publickey
        self.vmData = _vmData
        self.fileName = _fileName
        self.vncAccessInfo = _vncAccessInfo
        self.fileMode = _fileMode
        self.drDrillOption = _drDrillOption
        self.uuid = _uuid
        self.isMultiDiskSpeedup = _isMultiDiskSpeedup
        self.fileNames = _fileNames
        self.vmDatas = _vmDatas
