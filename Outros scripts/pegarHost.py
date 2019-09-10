# Esse script recupera os hosts pelo id de grupo e pega o IP + DNS + grupo


# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time


zapi = ZabbixAPI("**********************************")
# Disable SSL certificate verification
zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 10.1
# informacoes de acesso
zapi.login("USER", "PASS")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

for hosts in zapi.host.get({
'groupids':'983',
'output': ['host','status'],
'selectInterfaces': ['ip', 'dns'],
'selectGroups': ['name']
}):
    print(hosts)

