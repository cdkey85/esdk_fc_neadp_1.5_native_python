'''
Created on 2015-3-7

@author: lWX232078
'''

class QueryDatastoreVolumeResp(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    quantityGB = None
    status = None
    isThin = None
    type = None
    vmName = None
    vmUrn = None
    vmStatus = None
    clusterName = None
    clusterUrn = None
    isDiffVol = None
    persistentDisk = None
    volType = None
    pciType = None
    ioWeight = None



    def __init__(self, 
                _urn = None,
                _uri = None,
                _name = None,
                _quantityGB = None,
                _status = None,
                _isThin = None,
                _type = None,
                _vmName = None,
                _vmUrn = None,
                _vmStatus = None,
                _clusterName = None,
                _clusterUrn = None,
                _isDiffVol = None,
                _persistentDisk = None,
                _volType = None,
                _pciType = None,
                _ioWeight = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.quantityGB = _quantityGB
        self.status = _status
        self.isThin = _isThin
        self.type = _type
        self.vmName = _vmName
        self.vmUrn = _vmUrn
        self.vmStatus = _vmStatus
        self.clusterName = _clusterName
        self.clusterUrn = _clusterUrn
        self.isDiffVol = _isDiffVol
        self.persistentDisk = _persistentDisk
        self.volType = _volType
        self.pciType = _pciType
        self.ioWeight = _ioWeight