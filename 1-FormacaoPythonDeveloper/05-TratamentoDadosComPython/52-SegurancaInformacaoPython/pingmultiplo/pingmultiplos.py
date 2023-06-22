import os
import time


with open ('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        #print(ip)
        print(f'Verificando o ip {ip}')
        os.system(f'ping -n 2 {ip}')
        print ('*' * 80)

        os.system(f'ping {ip}')
        print ('*' * 80)
        time.sleep(3)
