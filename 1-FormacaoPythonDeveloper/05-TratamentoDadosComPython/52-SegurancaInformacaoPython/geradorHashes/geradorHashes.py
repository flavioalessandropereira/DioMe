import hashlib

print('-=' * 60)
string = input('Digite o texto a ser gerado a hash: ')
print('-=' * 60)

while True:
    menu = int(input('''
    ### MENU - ESCOLHA O TIPO DE HASH ###
    [1] MD5
    [2] SHA1
    [3] SHA256
    [4] SHA512
    [5] SAIR
    Digite o numero no hash a ser gerado: 
    '''))

    print('-=' * 60)

    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print(f'O hash MD5 da string: {string} é: ', resultado.hexdigest())
        print('-=' * 60)

    elif menu == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print(f'O hash SHA1 da string {string} é: ', resultado.hexdigest())
        print('-=' * 60)

    elif menu == 3:
        resultado = hashlib.sha256 (string.encode('utf-8'))
        print(f'O hash SHA256 da string {string} é: ', resultado.hexdigest())
        print('-=' * 60)

    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print(f'O hash SHA512 da string {string} é: ', resultado.hexdigest())
        print('-=' * 60)

    elif menu == 5:
        print('Saindo do programa, OBRIGADO!')
        break
    else:
        print('Escolha uma opcao do MENU!')
        print('-=' * 60)