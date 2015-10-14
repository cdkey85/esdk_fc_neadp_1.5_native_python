'''
Created on 2015-3-7

@author: lWX232078
'''
from com.huawei.model.host.HostBasicInfo import HostBasicInfo

class QueryHostListResp(object):
    '''
    classdocs
    '''
    total = None
    hosts = [None]


    def __init__(self, _total=None,_hosts=[None]):
        '''
        Constructor
        '''
        self.total = _total
        self.hosts = _hosts