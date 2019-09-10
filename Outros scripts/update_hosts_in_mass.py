#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
import csv

zapi = ZabbixAPI(server="http://192.168.56.3/zabbix")
zapi.login("Admin", "zabbix")

hosts = zapi.host.get({"output": ["hostid","name"], "sortfield": "name"})

f = csv.reader(open('/home/mudarnome.csv'), delimiter=';')

for x in hosts: 
host_antigo.appen(x)

	for ["nomevelho","nomenovo"] in f:
	host_novo.appen(y)	
		if x["name"]==["nomevelho"]:
						
#			zapi.host.update({["nomenovo"]})

			print x["name"]

#	for [group] in f:
#    		print "Atualizando host da linha ", f.line_num
#		hostatualizado = zapi.host.update({[group]})

