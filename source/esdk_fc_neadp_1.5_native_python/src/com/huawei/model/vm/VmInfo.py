'''
Created on 2015-3-6

@author: sWX231817
'''

from com.huawei.model.vm.OsOption import OsOption
from com.huawei.model.vm.VmConfig import VmConfig
from com.huawei.model.vm.VmRebootConfig import VmRebootConfig
from com.huawei.model.vm.VncAccessInfo import VncAccessInfo


class VmInfo(object):
    '''
    classdocs
    '''
    uri = None
    urn = None
    uuid = None
    name = None
    description = None
    group = None
    location = None
    locationName = None
    hostUrn = None
    clusterUrn = None
    dataStoreUrns = [None]
    status = None
    pvDriverStatus = None
    toolInstallStatus = None
    cdRomStatus = None
    isTemplate = None
    isLinkClone = None
    createTime = None
    vncAccessInfo = VncAccessInfo()
    vmConfig = VmConfig()
    vmRebootConfig = VmRebootConfig()
    osOptions = OsOption()
    idle = None
    deleteTime = None
    toolsVersion = None
    imcSetting = None
    minCompatibleimcSetting = None
    isBindingHost = None
    additionalStatus = [None]
    hostName = None
    clusterName = None
    vmType = None
    drStatus = None
    rpoStatus = None
    initSyncStatus = None
    drDrillVmUri = None
    drDrillVmUrn = None
    objectPrivs = [None]


    def __init__(self, _uri=None, _urn=None, _uuid=None, _name=None, _description=None, _group=None, _location=None,
                  _locationName=None, _hostUrn=None, _clusterUrn=None, _dataStoreUrns=None, _status=None, _pvDriverStatus=None,
                   _toolInstallStatus=None, _cdRomStatus=None, _isTemplate=None, _isLinkClone=None, _createTime=None, _vncAccessInfo=None,
                    _vmConfig=None, _vmRebootConfig=None, _osOptions=None, _idle=None, _deleteTime=None, _toolsVersion=None, _imcSetting=None,
                     _minCompatibleimcSetting=None, _isBindingHost=None, _additionalStatus=None, _hostName=None, _clusterName=None, _vmType=None,
                      _drStatus=None, _rpoStatus=None, _initSyncStatus=None, _drDrillVmUri=None, _drDrillVmUrn=None, _objectPrivs=None):
        '''
        Constructor
        '''
        self.uri = _uri
        self.urn = _urn
        self.uuid = _uuid
        self.name = _name
        self.description = _description
        self.group = _group
        self.location = _location
        self.locationName = _locationName
        self.hostUrn = _hostUrn
        self.clusterUrn = _clusterUrn
        self.dataStoreUrns = _dataStoreUrns
        self.status = _status
        self.pvDriverStatus = _pvDriverStatus
        self.toolInstallStatus = _toolInstallStatus
        self.cdRomStatus = _cdRomStatus
        self.isTemplate = _isTemplate
        self.isLinkClone = _isLinkClone
        self.createTime = _createTime
        self.vncAccessInfo = _vncAccessInfo
        self.vmConfig = _vmConfig
        self.vmRebootConfig = _vmRebootConfig
        self.osOptions = _osOptions
        self.idle = _idle
        self.deleteTime = _deleteTime
        self.toolsVersion = _toolsVersion
        self.imcSetting = _imcSetting
        self.minCompatibleimcSetting = _minCompatibleimcSetting
        self.isBindingHost = _isBindingHost
        self.additionalStatus = _additionalStatus
        self.hostName = _hostName
        self.clusterName = _clusterName
        self.vmType = _vmType
        self.drStatus = _drStatus
        self.rpoStatus = _rpoStatus
        self.initSyncStatus = _initSyncStatus
        self.drDrillVmUri = _drDrillVmUri
        self.drDrillVmUrn = _drDrillVmUrn
        self.objectPrivs = _objectPrivs
