# -*- coding: utf-8 -*-

from spyne import rpc,Application,ServiceBase
from spyne import String,Unicode,Array,ComplexModel,Integer,table,Iterable
import json

class TestService(ServiceBase):
    @rpc(String,_returns=Iterable(String))
    def get_test(self,test_name):
        try:
            print(test_name)
            yield json.dumps({'name':test_name})
        except:
            yield 'error'



