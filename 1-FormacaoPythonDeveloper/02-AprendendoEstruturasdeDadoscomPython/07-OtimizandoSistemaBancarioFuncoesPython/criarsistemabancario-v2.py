import textwrap

def traco():
   print('=-=' * 15)

def menu():
   menu = '''\n
   ========================= MENU =========================
   [ d ]\t - Depositar
   [ s ]\t - Sacar
   [ e ]\t - Extrato
   [ nu ]\t - Novo Usuario
   [ nc ]\t - Nova Conta
   [ lc ]\t - Listar Contas
   [ q ]\t - Sair
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

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # colocando o * força informar de forma nomeada as variáveis
   excedeu_saldo = valor > saldo
   execedeu_limite = valor > limite
   excedeu_saques = numero_saques >= limite_saques

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

   return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): # saldo está como posicional(positional only) e o extrato de forma nomeada (keyboard only)
   print('\n=========== EXTRATO ===========')
   print('Não foram realizado movimentações.' if not extrato else extrato)
   print(f'\nSaldo:\t\tR$ {saldo:.2f}')
   print('======================')

def criar_usuario(usuarios):
   cpf = input('Informe o CPF (somente números): ')
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print('+++ CPF já cadastrado! +++')
      return
   
   nome = input('Informe Nome Completo: ')
   data_nascimento = input('Informe data de nascimetno (dd-mm-aaa): ')
   endereco = input('Informe o endereço (logradouro, número, bairro, cidade/sigla estado): ')

   usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf': cpf, 'endereco':endereco})

   print('**** Usuário criado com sucesso! ****')


def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
   return usuarios_filtrados[0]if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
   cpf = input('Informe o CPF do cliente: ')
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print('===== Conta criada com sucesso =====')
      return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario':usuario}
   
   print('++++ Usuário não encontrado, fluco de criação de conta ENCERRADO ! ++++')


def listar_contas(contas):
   for conta in contas:
      linha = f'''\
      Agencia:\t{conta['agencia']}
      C/C:\t\t{conta['numero_conta']}
      Titular: \t{conta['usuario']['nome']}
      '''
      print('=' * 100)
      print(textwrap.dedent(linha))



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

      if opcao == 'd':
         valor = float(input('Valor do depósito: R$ '))

         saldo, extrato = depositar (saldo,valor, extrato)


      elif opcao == 's':
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

      elif opcao == 'e': # extrato
         exibir_extrato (saldo, extrato = extrato)
      
      elif opcao == 'nu': # novo cliente
         criar_usuario (usuarios)
      
      elif opcao == 'nc': # nova conta
         numero_conta  = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)
         
         if conta:
            contas.append(conta)
      
      elif opcao == 'lc': # listar contas
         listar_contas (contas)


      elif opcao == 'q': # sair
         traco()
         print('Saindo do sistema, obrigado por utilizar!')
         break
         
      else:
         print('Operação inválida. Por favor selecione novamente a operação desejada.')



main()

      