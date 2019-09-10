from ZabbixSender import ZabbixSender, ZabbixPacket

# Definir informacoes sobre o server. 
server = ZabbixSender(server='192.168.120.96', port='10051')

packet = ZabbixPacket()
packet.add('A-SRV121','sendertrap', '10')

#server.send(packet)
server.send(packet)

print(server.status)
