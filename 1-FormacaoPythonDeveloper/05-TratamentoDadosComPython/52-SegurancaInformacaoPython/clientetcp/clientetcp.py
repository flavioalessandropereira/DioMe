import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('A conexao falhou.')
        print(f'Erro: {e}')
        sys.exit()

    print('Socket criado com sucesso')


    HostAlvo = input('Digite o Host ou Ip a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))

        print(f'Clientre TCP conectado com sucesso no Host: {HostAlvo}  e na Porta: {PortaAlvo}.')

        s.shutdown(2)

    except socket.error as e:
        print(f'Nao foi possivel conectar no HOST: {HostAlvo} na POrta: {PortaAlvo} ')
        print(f'Erro: {e}')
        sys.exit()

if __name__ == "__main__":
    main()