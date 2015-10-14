# coding=utf-8
'''
Created on 2015-3-9

@author: lWX232078
'''

from com.huawei.client.connection import RestClient
from com.huawei.model.task.TaskInfo import TaskInfo

class TaskResource(object):
    '''
    classdocs
    '''
    global client
    client = RestClient()

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def queryTask(self, task_uri):
        '''
        function:查询任务
        '''
        response = client.send(method='GET', url=task_uri, body=None, resp=TaskInfo(), name="queryTask")
        return response
        
