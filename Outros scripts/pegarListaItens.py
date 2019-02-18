# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
import urllib2


zapi = ZabbixAPI("https://sm-fe01.webmonitor.global")
# Disable SSL certificate verification
#zapi.session.verify = False
# Specify a timeout (in seconds)
#zapi.timeout = 30.1
# informacoes de acesso
zapi.login("linx.rafael", "stk456rfs")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

resultado = zapi.item.get({'output': 'extend', 
    'filter': {
        'state': 1}, 'monitored': False})
#print('Quantidade de itens nao suportado, somente hosts ativos: ', resultado)
for x in resultado:
    #zapi.item.update({'itemid': x ['itemid'],'status':1})
    print(x)