# coding = UTF-8
'''
Created on 2015-3-7

@author: y00206201
'''

from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient
from com.huawei.resources.cluster.ClusterResource import ClusterResource


if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');

    
    clutser = ClusterResource()
    #b = clutser.queryCluster('/service/sites/4D9D0815/clusters/79')
    
   
    b = clutser.queryClusters('/service/sites/4D9D0815',clusterUrns='urn2')
    print b
    
    login.logout()