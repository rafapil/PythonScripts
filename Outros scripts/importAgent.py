# estrutura para incluir hosts automaticamente para AGENT-ZABBIX
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
import csv

# URL do Zabbix
zapi = ZabbixAPI("https://sm-fe01.webmonitor.global")
# Disabilita o SSL
zapi.session.verify = False
# Tempo de timeout (em segundos)
zapi.timeout = 10.1
# informacoes de acesso
zapi.login("linx.rafael", "stk456rfs")

# Aqui entra a parte responsavel por fazer o insert do .csv
f = csv.reader(open('D:/import/import.csv'), delimiter=';') # faz a leitura do arquivo com separador por ; 

for [hostname, ip, dns, port, groupID, templateID] in f: # sao adicionados 6 colunas responsaveis por: hostname, ip, dns, porta, id do grupo e id do template
    zapi.host.create({"host": hostname, 
      "interfaces": [ {"type": "1",
       "main": "1",
      "useip": "1",
      "ip":ip,
      "dns": dns,
      "port": port}], 
      "groups": [{ "groupid": groupID}], #id do host grupo
      "templates": [{ "templateid": templateID}] #id do template

   })

