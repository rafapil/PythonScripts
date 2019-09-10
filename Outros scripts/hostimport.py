# estrutura para incluir hosts automaticamente para SNMP
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
import csv

# URL do Zabbix
zapi = ZabbixAPI("*********************************")
zapi.login("USER", "PASS")

zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 120000.1

# Aqui entra a parte responsavel por fazer o insert do .csv
print("Processo iniciado")
f = csv.reader(open('C:/Import/import.csv'), delimiter=';') # faz a leitura do arquivo com separador por ; 

for [hostname, ip, dns, port, groupID, templateID] in f: # sao adicionados 6 colunas responsaveis por: hostname, ip, dns, porta, id do grupo e id do template
    zapi.host.create({"host": hostname, 
      "interfaces": [ {"type": "2", # type 1 para agent | type 2 para snmp
      "main": "1",
      "useip": "1",
      "ip":ip,
      "dns": dns,
      "port": port}], 
      "groups": [{ "groupid": groupID}], #id do host grupo
      "templates": [{ "templateid": templateID}] #id do template
   })
print("Processo Finalizado")