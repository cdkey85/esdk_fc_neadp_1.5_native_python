'''
Created on 2015-3-7

@author: lWX232078
'''

class HostDNSCfg(object):
    '''
    classdocs
    '''
    primaryDNSIp = None
    secondaryDNSIps = [None]
    domainName = None


    def __init__(self, _primaryDNSIp = None,_secondaryDNSIps = [None],_domainName = None):
        '''
        Constructor
        '''
        self.primaryDNSIp = _primaryDNSIp
        self.secondaryDNSIps = _secondaryDNSIps
        self.domainName = _domainName