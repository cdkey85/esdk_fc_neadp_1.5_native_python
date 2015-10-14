'''
Created on 2015-3-10

@author: sWX231817
'''

class VolSnapshot(object):
    '''
    classdocs
    '''
    volumeUrn = None
    volumeUri = None
    storageType = None
    datastoreUrn = None
    snapUuid = None
    snapNameOnDev = None
    snapIscsi = None
    sdUrn = None
    sdUri = None
    volCBTCreateTime = None
    ChgID = None

    def __init__(self, _volumeUrn=None, _volumeUri=None, _storageType=None, _datastoreUrn=None, _snapUuid=None, _snapNameOnDev=None,
                  _snapIscsi=None, _sdUrn=None, _sdUri=None, _volCBTCreateTime=None, _ChgID=None):
        '''
        Constructor
        '''
        self.volumeUrn = _volumeUrn
        self.volumeUri = _volumeUri
        self.storageType = _storageType
        self.datastoreUrn = _datastoreUrn
        self.snapUuid = _snapUuid
        self.snapNameOnDev = _snapNameOnDev
        self.snapIscsi = _snapIscsi
        self.sdUrn = _sdUrn
        self.sdUri = _sdUri
        self.volCBTCreateTime = _volCBTCreateTime
        self.ChgID = _ChgID
