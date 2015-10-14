# coding=utf-8
'''
Created on 2015-3-7

@author: y00206201
'''
import sys 

sys.path.append("..")

from com.huawei.client.log import *
from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient
from com.huawei.resources.cluster.ClusterResource import ClusterResource
from com.huawei.model.cluster.QueryClusterListReq import  QueryClusterListReq

import hashlib

if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');
    LogInit(LogConf('../../log.conf','LOGCONF'))
    
    clutser = ClusterResource()
    
    
    b = clutser.queryCluster('/service/sites/4D9D0815/clusters/79')

    print '-------------------------------------------------------'
    req = QueryClusterListReq()
    #req.clusterUrns = ['urn:sites:4D9D0815:clusters:79']
    b = clutser.queryClusterList('/service/sites/4D9D0815',req) 
    login.logout()