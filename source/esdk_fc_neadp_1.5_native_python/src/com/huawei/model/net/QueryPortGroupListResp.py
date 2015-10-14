'''
Created on 2015-3-10

@author: lWX232078
'''

class QueryPortGroupListResp(object):
    '''
    classdocs
    '''
    total=None
    portGroups=[None]


    def __init__(self, _total=None,_portGroups=[None]):
        '''
        Constructor
        '''
        self.total = _total
        self.portGroups = _portGroups 