'''
Created on 2015-3-7

@author: lWX232078
'''
import CpuUsage
import MemUsage

class HostBasicInfo(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    description = None
    ip = None
    bmcIp = None
    bmcUserName = None
    clusterUrn = None
    clusterName = None
    status = None
    isMaintaining = None
    multiPathMode = None
    hostMultiPathMode = None
    memQuantityMB = None
    cpuQuantity = None
    nicQuantity = None
    cpuMHz = None
    attachedISOVMs = [None]
    computeResourceStatics = None
    ntpIp1 = None
    ntpIp2 = None
    ntpIp3 = None
    ntpCycle = None
    physicalCpuQuantity = None
    gpuCapacity = None
    gpuCapacityReboot = None
    imcSetting = None
    maxImcSetting = None
    cpuResource = None
    memResource = None
    gdvmMemory = None
    gdvmMemoryReboot = None
    gsvmMemory = None
    gsvmMemoryReboot = None
    haState = None
    haRole = None
    isFailOverHost = None



    def __init__(self,    _urn = None,
    _uri = None,
    _name = None,
    _description = None,
    _ip = None,
    _bmcIp = None,
    _bmcUserName = None,
    _clusterUrn = None,
    _clusterName = None,
    _status = None,
    _isMaintaining = None,
    _multiPathMode = None,
    _hostMultiPathMode = None,
    _memQuantityMB = None,
    _cpuQuantity = None,
    _nicQuantity = None,
    _cpuMHz = None,
    _attachedISOVMs = [None],
    _computeResourceStatics = None,
    _ntpIp1 = None,
    _ntpIp2 = None,
    _ntpIp3 = None,
    _ntpCycle = None,
    _physicalCpuQuantity = None,
    _gpuCapacity = None,
    _gpuCapacityReboot = None,
    _imcSetting = None,
    _maxImcSetting = None,
    _cpuResource = None,
    _memResource = None,
    _gdvmMemory = None,
    _gdvmMemoryReboot = None,
    _gsvmMemory = None,
    _gsvmMemoryReboot = None,
    _haState = None,
    _haRole = None,
    _isFailOverHost = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.description = _description
        self.ip = _ip
        self.bmcIp = _bmcIp
        self.bmcUserName = _bmcUserName
        self.clusterUrn = _clusterUrn
        self.clusterName = _clusterName
        self.status = _status
        self.isMaintaining = _isMaintaining
        self.multiPathMode = _multiPathMode
        self.hostMultiPathMode = _hostMultiPathMode
        self.memQuantityMB = _memQuantityMB
        self.cpuQuantity = _cpuQuantity
        self.nicQuantity = _nicQuantity
        self.cpuMHz = _cpuMHz
        self.attachedISOVMs = _attachedISOVMs
        self.computeResourceStatics = _computeResourceStatics
        self.ntpIp1 = _ntpIp1
        self.ntpIp2 = _ntpIp2
        self.ntpIp3 = _ntpIp3
        self.ntpCycle = _ntpCycle
        self.physicalCpuQuantity = _physicalCpuQuantity
        self.gpuCapacity = _gpuCapacity
        self.gpuCapacityReboot = _gpuCapacityReboot
        self.imcSetting = _imcSetting
        self.maxImcSetting = _maxImcSetting
        self.cpuResource = _cpuResource
        self.memResource = _memResource
        self.gdvmMemory = _gdvmMemory
        self.gdvmMemoryReboot = _gdvmMemoryReboot
        self.gsvmMemory = _gsvmMemory
        self.gsvmMemoryReboot = _gsvmMemoryReboot
        self.haState = _haState
        self.haRole = _haRole
        self.isFailOverHost = _isFailOverHost
