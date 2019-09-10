from pyzabbix import ZabbixMetric, ZabbixSender

valor = 1

packet = [
  ZabbixMetric('A-SRV121', 'sendertrap', valor),
]

result = ZabbixSender(zabbix_server='192.168.120.96', zabbix_port=10051, use_config=None, chunk_size=250, socket_wrapper=None, timeout=10).send(packet)
