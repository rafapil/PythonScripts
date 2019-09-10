# estrutura para incluir hosts automaticamente para SNMP
from zabbix_api import ZabbixAPI
# from datetime import datetime
# import time
# import csv

# URL do Zabbix
zapi = ZabbixAPI("******************************")
zapi.login("USER", "PASS")

zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 120000.1

# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

resultado = zapi.item.get({
    "groupids":"1195", # O grupo deve ser informado nesta parte do código. 
    "filter":{
        "state":1
    },
    "output":[
        "hostid",
        "name",
        "itemid"
    ],
    "monitored": True  
})
#print('Quantidade de itens nao suportado, somente hosts ativos: ', resultado)
for x in resultado:
    zapi.item.update({'itemid': x ['itemid'],'status':1})
    print (x['itemid'])