# -*- coding: utf-8 -*-

from spyne import rpc,Application,ServiceBase
from spyne import String,Unicode,Array,ComplexModel,Integer,table,Iterable


class TestService(ServiceBase):

    @rpc(String,_returns=Iterable(String))
    def get_test(self,test_name):
        try:
            yield 'name'+test_name
        except:
            yield 'error'



