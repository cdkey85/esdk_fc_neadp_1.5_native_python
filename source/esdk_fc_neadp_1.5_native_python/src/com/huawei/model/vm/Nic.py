'''
Created on 2015-3-6

@author: sWX231817
'''

class Nic(object):
    '''
    classdocs
    '''
    name = None
    urn = None
    uri = None
    portGroupUrn = None
    portGroupName = None
    mac = None
    ip = [None]
    ips6 = [None]
    sequenceNum = None
    virtIo = None
    ipList = None
    nicType = None



    def __init__(self, _name=None, _urn=None, _uri=None, _portGroupUrn=None, _portGroupName=None, _mac=None, _ip=None, _ips6=None,
                  _sequenceNum=None, _virtIo=None, _ipList=None, _nicType=None):
        '''
        Constructor
        '''
        self.name = _name
        self.urn = _urn
        self.uri = _uri
        self.portGroupUrn = _portGroupUrn
        self.portGroupName = _portGroupName
        self.mac = _mac
        self.ip = _ip
        self.ips6 = _ips6
        self.sequenceNum = _sequenceNum
        self.virtIo = _virtIo
        self.ipList = _ipList
        self.nicType = _nicType
