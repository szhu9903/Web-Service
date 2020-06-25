# -*- coding: utf-8 -*-

from spyne import rpc,ServiceBase
from spyne import String,Unicode,Array,ComplexModel,Integer,table,Iterable
import json

class TestService(ServiceBase):
    @rpc(String,Unicode,_returns=String)
    def hello_test(self,test_name,data_json):
        try:
            print(test_name)
            print(data_json)
            return json.dumps({
                'success':1,
                'state':'200',
                'msg':'获取成功',
                'data':[{'name':'szhu','age':'1'},{'name':'n','age':'0'}],
                'cs':data_json
            })
        except:
            return json.dumps({
                'success':0,
                'state':'500',
                'msg':'异常'
            })



