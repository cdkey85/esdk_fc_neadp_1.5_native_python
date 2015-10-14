'''
Created on 2015-3-13

@author: sWX231817
'''

class OsInfo(object):
    '''
    classdocs
    '''
    id = None
    versionDes = None
    cpuQuantityLimit = None
    cpuSocketLimit = None
    memQuantityLimit = None
    supportCpuHotPlug = None
    supportMemHotPlug = None


    def __init__(self, _id=None, _versionDes=None, _cpuQuantityLimit=None, _cpuSocketLimit=None, _memQuantityLimit=None,
                 _supportCpuHotPlug=None, _supportMemHotPlug=None):
        '''
        Constructor
        '''
        self.id = _id
        self.versionDes = _versionDes
        self.cpuQuantityLimit = _cpuQuantityLimit
        self.cpuSocketLimit = _cpuSocketLimit
        self.memQuantityLimit = _memQuantityLimit
        self.supportCpuHotPlug = _supportCpuHotPlug
        self.supportMemHotPlug = _supportMemHotPlug
