'''
Created on 2015-3-7

@author: lWX232078
'''

class PortGroup(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    subnetUrn = None
    portType = None
    vlanId = None
    vxlanId = None
    vlanRange = None
    adminStatus = None
    description = None
    txLimit = None
    txPeakLimit = None
    txBurstSize = None
    txWeight = None
    priority = None
    rxLimit = None
    rxPeakLimit = None
    rxBurstSize = None
    isDhcpIsolation = None
    isIpMacBind = None
    isEnablePG = None
    vspNum = None
    multicastIp = None
    arpBcstSuppress = None
    ipBcstSuppress = None



    def __init__(self, _urn = None,
    _uri = None,
    _name = None,
    _subnetUrn = None,
    _portType = None,
    _vlanId = None,
    _vxlanId = None,
    _vlanRange = None,
    _adminStatus = None,
    _description = None,
    _txLimit = None,
    _txPeakLimit = None,
    _txBurstSize = None,
    _txWeight = None,
    _priority = None,
    _rxLimit = None,
    _rxPeakLimit = None,
    _rxBurstSize = None,
    _isDhcpIsolation = None,
    _isIpMacBind = None,
    _isEnablePG = None,
    _vspNum = None,
    _multicastIp = None,
    _arpBcstSuppress = None,
    _ipBcstSuppress = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.subnetUrn = _subnetUrn
        self.portType = _portType
        self.vlanId = _vlanId
        self.vxlanId = _vxlanId
        self.vlanRange = _vlanRange
        self.adminStatus = _adminStatus
        self.description = _description
        self.txLimit = _txLimit
        self.txPeakLimit = _txPeakLimit
        self.txBurstSize = _txBurstSize
        self.txWeight = _txWeight
        self.priority = _priority
        self.rxLimit = _rxLimit
        self.rxPeakLimit = _rxPeakLimit
        self.rxBurstSize = _rxBurstSize
        self.isDhcpIsolation = _isDhcpIsolation
        self.isIpMacBind = _isIpMacBind
        self.isEnablePG = _isEnablePG
        self.vspNum = _vspNum
        self.multicastIp = _multicastIp
        self.arpBcstSuppress = _arpBcstSuppress
        self.ipBcstSuppress = _ipBcstSuppress