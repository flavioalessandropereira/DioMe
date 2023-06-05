import textwrap

def traco():
   print('=-=' * 15)

def menu():
   menu = '''\n
   ========================= MENU =========================
   [ 1 ]\t - Depositar
   [ 2 ]\t - Sacar
   [ 3 ]\t - Extrato
   [ 4 ]\t - Novo Usuario
   [ 5 ]\t - Nova Conta
   [ 6 ]\t - Listar Contas
   [ 0 ]\t - Sair
   '''
   return input (textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/): # por ter o simbolo / os valores são passados por posição
   if valor > 0:
      saldo += valor
      extrato += f'Depósito:\tR$ {valor:.2f}\n'
      print('**** Depósito realizado com sucesso! ****')
          
   else:
      print('+++ Falha na operação. Valor informado inválido! +++')

   return saldo, extrato



def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
   excedeu_saldo = valor > saldo
   execedeu_limite = valor > limite
   excedeu_saques = numeros_saques >= limite_saques

   if excedeu_saldo:
      print('\n+++ Falha na operação. Não tem saldo suficiente! +++')
   
   elif execedeu_limite:
      print('\n+++ Falha na operação. Valor do saque excede o limite diário! +++')
   
   elif excedeu_saques:
      print('\n+++ Falha na operação. Número de saques/dia excedido! +++')

   elif valor > 0:
      saldo -= valor
      extrato += f"Saque:\t\tR$ {valor:.2f}\n"
      numero_saques += 1
      print('\n**** Saque realizado com sucesso! ****')

   else:
      print('+++ Falha na operação. Valor informado inválido! +++')


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
            limite_saques = LIMITE_SAQUES,
         )

      elif opcao == 3: # extrato
         exibir_extrato (saldo, extrato = extrato)
      
      elif opcao == 4: # novo cliente
         criar_usuario = (usuarios)
      
      elif opcao == 5: # nova conta
         numero_conta  = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)
         
         if conta:
            contas.append(conta)
      
      elif opcao == 6: # listar contas
         listar_contas (contas)


      elif opcao == 0: # sair
         traco()
         print('Saindo do sistema, obrigado por utilizar!')
         break
         
      else:
         print('Operação inválida. Por favor selecione novamente a operação desejada.')





      