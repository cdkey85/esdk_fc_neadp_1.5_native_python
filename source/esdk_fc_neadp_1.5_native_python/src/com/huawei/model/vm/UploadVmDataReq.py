'''
Created on 2015-3-6

@author: sWX231817
'''

class UploadVmDataReq(object):
    '''
    classdocs
    '''
    vmData = None
    fileName = None 


    def __init__(self, _vmData=None, _fileName=None):
        '''
        Constructor
        '''
        self.vmData = _vmData
        self.fileName = _fileName
