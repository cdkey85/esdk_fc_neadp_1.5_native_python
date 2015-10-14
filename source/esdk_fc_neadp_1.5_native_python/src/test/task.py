import sys 
sys.path.append("..")

from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient

from com.huawei.resources.task.TaskResource import TaskResource

if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');
    
    
    task = TaskResource()   
    b = task.queryTask('/service/sites/4D9D0815/tasks/18439')
    print b
    
    login.logout()
