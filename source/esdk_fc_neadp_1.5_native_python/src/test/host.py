import sys 
sys.path.append("..")

from com.huawei.client.log import *
from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient

from com.huawei.resources.host.HostResource import HostResource
from com.huawei.model.host.QueryHostListReq import QueryHostListReq
from com.huawei.model.host.QueryHostListResp import QueryHostListResp
from com.huawei.model.host.HostInfo import HostInfo

if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');
    LogInit(logCog = LogConf(confFile='../../log.conf',sec='LOGCONF'))
    
    host = HostResource()
    
    
    b = host.queryHost('/service/sites/4D9D0815/hosts/134')
   # print b
    
    print '--------------------------------------------------'
    req=QueryHostListReq()
    req.limit = 1
    req.offset = 0
    b = host.queryHostList('/service/sites/4D9D0815',req)
    
    #print b
    
    login.logout()