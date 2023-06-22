import os #importa o modulo ou biblioteca OS (integra os programas e recursos do Sistema Operacional

print('#' * 60)
ip_ou_host = input('Digite o Ip ou host a ser verificado: ') #exemplo: www.google.com
print('-' * 60)

os.system(f'ping -n 6 {ip_ou_host}') # chamando system da biblioteca "os" -  comando ping
# -n = numero de pacotes que são 6{}
print('-' * 60)

