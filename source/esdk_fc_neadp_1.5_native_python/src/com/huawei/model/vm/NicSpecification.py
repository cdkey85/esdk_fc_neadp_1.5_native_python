'''
Created on 2015-3-6

@author: sWX231817
'''

from com.huawei.model.vm.IpAddress6 import IpAddress6

class NicSpecification(object):
    '''
    classdocs
    '''
    sequenceNum = None
    ip = None
    netmask = None
    gateway = None
    setdns = None
    adddns = None
    ipVersion = None
    autoConfEnabled6 = None
    dhcpEnabled6 = None
    ipAddress6 = [IpAddress6()]
    gatewayIpAddr6 = None
    setdns6 = None
    adddns6 = None

    def __init__(self, _sequenceNum=None, _ip=None, _netmask=None, _gateway=None, _setdns=None, _adddns=None, _ipVersion=None,
                  _autoConfEnabled6=None, _dhcpEnabled6=None, _ipAddress6=None, _gatewayIpAddr6=None, _setdns6=None, _adddns6=None):
        '''
        Constructor
        '''
        self.sequenceNum = _sequenceNum
        self.ip = _ip
        self.netmask = _netmask
        self.gateway = _gateway
        self.setdns = _setdns
        self.adddns = _adddns
        self.ipVersion = _ipVersion
        self.autoConfEnabled6 = _autoConfEnabled6
        self.dhcpEnabled6 = _dhcpEnabled6
        self.ipAddress6 = _ipAddress6
        self.gatewayIpAddr6 = _gatewayIpAddr6
        self.setdns6 = _setdns6
        self.adddns6 = _adddns6
        