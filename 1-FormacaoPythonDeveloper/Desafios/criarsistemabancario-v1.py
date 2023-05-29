def traco():
   print('=-=' * 10)


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


  opcao = int(input('Digite a opção: '))
  

  if opcao == 1:
    traco()
    print('DEPÓSITO')
    deposito = float(input('Valor do depósito: R$ '))
    if deposito <= 0:
       print('Não é aceito depósito sendo 0 ou Valor Negativo')
    else:   
      saldo += deposito

  elif opcao == 2:
     print('sacar')

  elif opcao == 3:
     print(extrato)

  elif opcao == 0:
      traco()
      print('Saindo do sistema, obrigao por utilizar!')
      break
  else:
     print('Operação inválida. Por favor selecione novamente a operação desejada.')


print(f'Valor do Saldo em conta corrente: {saldo:.2f}')