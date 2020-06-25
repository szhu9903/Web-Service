
from suds.client import Client

wsdl = 'http://localhost:8001/?wsdl'

import json

def test_hello(url,name):
    client = Client(url)
    args = json.dumps({'name':'请求参数'})
    rs = client.service.hello_test(name,args)
    print(rs)

if __name__ == '__main__':
    test_hello(wsdl,'Hello Web-Service')






