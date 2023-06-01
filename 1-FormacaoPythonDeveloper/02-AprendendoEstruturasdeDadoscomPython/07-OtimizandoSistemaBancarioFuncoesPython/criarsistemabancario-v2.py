import textwrap

def traco():
   print('=-=' * 15)

def menu():
   menu = '''\n
   ========================= MENU =========================
   [ 1 ] - Depositar
   [ 2 ] - Sacar
   [ 3 ] - Extrato
   [ 4 ] - Novo Usuario
   [ 5 ] - Nova Conta
   [ 6 ] - Listar Contas
   [ 0 ] - Sair
   '''
   return input (textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
   if valor > 0:
      saldo += valor
      extrato += f'Depósito:\tR$ {valor:.2f}\n'
      print('**** Depósito realizado com sucesso! ****')
          
   else:
      print('+++ Falha na operação. Valor informado inválido! +++')

   return saldo, extrato


def main():
   LIMITE_SAQUES = 3
   AGENCIA = '0001'

   saldo = 0
   limite = 500
   extrato = ''
   numero_saques = 0
   usuarios = []
   contas = []

   while True:
      opcao = menu()

      if opcao == 1:
         valor = float(input('Valor do depósito: R$ '))

         saldo, extrato = depositar (saldo,valor, extrato)


      elif opcao == 2:
         traco()
         print('SACAR')
         valor = float(input('Valor do saque: R$ '))

         saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES
         )

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





      