# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

from spyne import Application
# soap协议
from spyne.protocol.soap import Soap11
# 测试
from spyne.server.wsgi import WsgiApplication


applicaction = Application([],
                           'mytest',
                           in_protocol = Soap11(validator = 'lxml'),
                           out_protocol = Soap11())
wsgi_application = WsgiApplication(applicaction)

if __name__ == '__main__':
    import logging

    host = '0.0.0.0'
    port = 8001

    logging.info('listening to http://127.0.0.1:8001')
    logging.info('wsdl is at: http://127.0.0.1:8001/?wsdl')

    server = make_server(host,port,wsgi_application)
    server.serve_forever()



