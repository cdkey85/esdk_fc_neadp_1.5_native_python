'''
Created on 2015-3-7

@author: sWX231817
'''

from com.huawei.model.vm.AsynchrTask import AsynchrTask

class VmTaskResp(AsynchrTask):
    '''
    classdocs
    '''
    urn = None
    uri = None

    def __init__(self, _urn=None, _uri=None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri 
