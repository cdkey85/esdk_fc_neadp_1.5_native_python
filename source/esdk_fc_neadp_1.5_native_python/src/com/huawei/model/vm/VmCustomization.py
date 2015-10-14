'''
Created on 2015-3-6

@author: sWX231817
'''
from com.huawei.model.vm.NicSpecification import NicSpecification

class VmCustomization(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    description = None
    osType = None
    hostname = None
    password = None
    workgroup = None
    domain = None
    domainName = None
    domainPassword = None
    nicSpecification = [NicSpecification()]
    ouName = None

    def __init__(self, _urn=None, _uri=None, _name=None, _description=None, _osType=None, _hostname=None, _password=None,
                  _workgroup=None, _domain=None, _domainName=None, _domainPassword=None, _nicSpecification=None, _ouName=None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.description = _description
        self.osType = _osType
        self.hostname = _hostname
        self.password = _password
        self.workgroup = _workgroup
        self.domain = _domain
        self.domainName = _domainName
        self.domainPassword = _domainPassword
        self.nicSpecification = _nicSpecification
        self.ouName = _ouName
