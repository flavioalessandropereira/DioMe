import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print (endereco)

print (endereco + 100)

print (endereco + 256)

print (endereco + 2000)

ip2 = '192.168.0.0/0'
rede = ipaddress.ip_network(ip2, strict=False)
for ip2 in rede:
    print(f'\nIP com REDE: {ip2}')