# estrutura para incluir hosts automaticamente para SNMP
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
import csv

# URL do Zabbix
# zapi = ZabbixAPI(server="http://zabbix-teste.com")
# zapi.login("admin", "senha")

zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 100000.1

# grupo modelo para filtrar com mais de um parametro 
def obterGrupoId(nomeGrupo):
     groupId = zapi.hostgroup.get({ "output": "extend", "search": { "name": nomeGrupo } })[0]['groupid']    
     return groupId

# print (obterGrupoId('HG000000000038/MeiosDePagamentos/Verti'))

# Aqui entra a parte responsavel por fazer o insert do .csv
print("Processo iniciado")
f = csv.reader(open('D:/import/import.csv'), delimiter=';') # faz a leitura do arquivo com separador por ; 

for [hostname, ip, dns, port, groupID01, groupID02, templateID01, templateID02, hostMACRO01, hostMACRO02, OSDesc] in f: # sao adicionados 6 colunas responsaveis por: hostname, ip, dns, porta, id do grupo e id do template
    zapi.host.create({"host": hostname, 
      "interfaces": [ {"type": "2", # type 1 para agent | type 2 para snmp
      "main": "1",
      "useip": "1",
      "ip":ip,
      "dns": dns,
      "port": port}], 
      "groups": [
                 {
                   "groupid": obterGrupoId(groupID01) # criar uma funcao que verifica o grupo 
                 },
                 {
                   "groupid": groupID02
                 }
      ], #id do host grupo
      "templates": [
                    {
                      "templateid": templateID01
                    },
                    {
                      "templateid": templateID02
                    }
      ],  #id do template
      "macros": [
                 {
                    "macro": "{$NETWORKID}", # a macro já esta definida por ser um projeto espcif.
                    "value": hostMACRO01
                 },
                 {
                    "macro": "{$SERIAL}", # a macro já esta definida por ser um projeto espcif.
                    "value": hostMACRO02
                 }
      ],
      "inventory_mode": 0,
      "inventory": {
            "os_full": OSDesc # info da maquina VM detalhamento que puxei do proprio csv que tirei do VMWare

        }
   })
   
print("Processo Finalizado")