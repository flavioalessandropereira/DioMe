def traco():
   print('=-=' * 15)


menu = '''
[ 1 ] - Depositar
[ 2 ] - Sacar
[ 3 ] - Extrato
[ 0 ] - Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  traco()
  print (menu)
  traco ()
  
  print()
  opcao = int(input('Digite a opção: '))
  print()

  if opcao == 1:
    traco()
    print('DEPÓSITO')
    valor = float(input('Valor do depósito: R$ '))

    if valor > 0:
       saldo += valor
       extrato += f'Depósito: R$ {valor:.2f}\n'

    else:
       print('Falha na operação. Informe um valor válido.')

  elif opcao == 2:
    traco()
    print('SACAR')
    valor = float(input('Valor do saque: R$ '))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
       print('Falha na operação de Saque. Saldo insuficiente.')
    
    elif excedeu_limite:
       print(f'Falha na operação de Saque. Limite R$ {limite}/saque.')
    
    elif excedeu_saque:
       print(f'Falha na operação de Saque. {LIMITE_SAQUES}/dia.')
         
    elif valor > 0:
       saldo -= valor
       extrato += f'Saque R$ {saldo:.2f}\n'
       numero_saques += 1


    else:   
      print('Falha na operação. Informe um valor válido.')


  elif opcao == 3:
     traco()
     print('\n*************** EXTRATO ***************')
     print('Sem movimentaçao na Conta' if not extrato else extrato)
     print(f'\nSaldo: R$ {saldo:.2f}\n')

  elif opcao == 0:
      traco()
      print('Saindo do sistema, obrigao por utilizar!')
      break
    
  else:
     print('Operação inválida. Por favor selecione novamente a operação desejada.')


