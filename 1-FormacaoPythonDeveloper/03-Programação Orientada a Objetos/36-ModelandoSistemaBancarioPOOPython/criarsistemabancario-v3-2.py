import textwrap
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
from datetime import datetime


class Cliente:
    
   def __init__(self, endereco) -> None:
      self.endereco = endereco
      self.contas = [] #lista

   def realizar_transacao(self, conta, transacao):
     transacao.registrar(conta)
   
   def adicionar_conta(self, conta):
      self.contas.append(conta)

   


class PessoaFisica(Cliente):
   def __init__(self, nome, data_nascimento, cpf, endereco):
      super().__init__(endereco)
      self.nome = nome
      self.data_nascimento = data_nascimento
      self.cpf = cpf



class Conta:
   def __init__(self, numero, cliente):
      self._saldo = 0
      self._numero = numero
      self._agencia = '0001'
      self._cliente = cliente
      self._historico = Historico()

   @classmethod
   def nova_conta(cls, cliente, numero):
      return cls(numero, cliente)
   

   @property
   def saldo(self):
      return self._saldo
   
   @property
   def numero (self):
      return self._numero
   
   @property
   def agencia(self):
      return self._agencia
   
   @property #acessar os metodos
   def cliente(self):
      return self._cliente
   
   @property
   def historico(self):
      return self._historico
   

   def sacar(self, valor):
      saldo = self.saldo
      excedeu_saldo = valor > saldo

      if excedeu_saldo:
         print('\n+++ Falha na operação. Não tem saldo suficiente! +++')
      
      elif valor > 0:
         self._saldo -= valor
         print('\n**** Saque realizado com sucesso! ****')
         return True
      
      else:
         print('+++ Falha na operação. Valor informado inválido! +++')

      return False


   def depositar(self, valor):
     
      if valor > 0:
         self._saldo += valor
         print('\n**** Depósito realizado com sucesso! ****')
     
      else:
         print('+++ Falha na operação. Valor informado inválido! +++')
         return False
      
      return True



class ContaCorrente(Conta):
   def __init__(self, numero, cliente, limite=500, limite_saques=3):
      super().__init__(numero, cliente)
      self.limite = limite
      self.limite_saques = limite_saques

   def sacar(self, valor):
      numero_saques = len(
         [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__ ]
      )

      excedeu_limite = valor > self.limite
      excedeu_saques = numero_saques >= self.limite_saques

      if excedeu_limite:
         print('\n+++ Falha na operação. O valor do saque excede o limite! +++')

      elif excedeu_saques:
         print('\n+++ Falha na operação. Número de saques/dia excedido! +++')
      
      else:
         return super().sacar(valor)\
      
      return False
   

   def __str__(self):
      return f"""\
         Agencia:\t{self.agencia}
         C/C:\t{self.numero}
         Titular:\t{self.cliente.nome}
      """

    

class Historico:
   def __init__(self):
      self._transacoes = [] #lista

   @property
   def transacoes(self):
      return self._transacoes
   
   def adicionar_transacao(self, transacao):
      self._transacoes.append( #dicionario
         {
            "tipo" : transacao.__class__.__name__,
            "valor" : transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),

         }
      )
    

class Transacao(ABC):
   @property
   @abstractproperty
   def valor(self):
      pass

   @abstractclassmethod
   def registrar(self, conta):
      pass
    

class Saque(Transacao):
   def __init__(self, valor):
      self._valor = valor
   
   @property
   def valor(self):
      return self._valor
   

   def registrar(self, conta):
      sucesso_transacao = conta.sacar(self.valor)

      if sucesso_transacao:
         conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
   def __init__(self, valor):
      self._valor = valor
   
   @property
   def valor(self):
      return self._valor
   

   def registrar(self, conta):
      sucesso_transacao = conta.depositar(self.valor)

      if sucesso_transacao:
         conta.historico.adicionar_transacao(self)

      
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


def filtrar_cliente(cpf, clientes):
   clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
   return clientes_filtrados[0] if clientes_filtrados else None



def recuperar_conta_cliente(cliente):
   if not cliente.contas:
      print('\n+++ Cliente nao possui conta! +++')
      return
   
   # FIXME: nao permite cliente escolher a conta
   return cliente.contas[0]


def depositar(clientes):
   cpf = input('Informe o CPF do cliente: ')
   cliente = filtrar_cliente(cpf, clientes)

   if not cliente:
      print('\n+++ Cliente nao cadastrado! +++')
      return
   
   valor = float(input('Informe o valor do Depósito: '))
   transacao = Deposito(valor)
   
   conta = recuperar_conta_cliente(cliente)
   if not conta:
      return
   
   cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
   cpf = input('Informe o CPF do cliente: ')
   cliente = filtrar_cliente(cpf, clientes)

   if not cliente:
      print('\n+++ Cliente nao cadastrado! +++')
      return
   
   valor = float(input('Informe o valor do Saque: '))
   transacao = Saque(valor)
   
   conta = recuperar_conta_cliente(cliente)
   if not conta:
      return
   
   cliente.realizar_transacao(conta, transacao)



def exibir_extrato(clientes):
   cpf = input('Informe o CPF do cliente: ')
   cliente = filtrar_cliente(cpf, clientes)

   if not cliente:
      print('\n+++ Cliente nao cadastrado! +++')
      return
   
   
   conta = recuperar_conta_cliente(cliente)
   if not conta:
      return
   
   print('\n=============== EXTRATO ===============')
   transacoes = conta.historico.transacoes

   extrato = ""
   if not transacoes:
      extrato = 'Nao foram realizadas movimentaçoes'

   else:
      for transacao in transacoes:
         extrato += f"\n{transacao[tipo]} : \n\tR$ {transacao['valor']:.2f}"
      
   
   print(extrato)
   print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
   print('\n=============== +++++++ ===============')

def criar_clientes(clientes):
   cpf = input('Informe o CPF do cliente: ')
   cliente = filtrar_cliente(cpf, clientes)

   if cliente:
      print('\n+++ CPF já cadastrado! +++')
      return
   
   nome = input('Informe nome por completo: ')
   data_nascimento = input('Informe a data de nascimento (dd-mm-aaa): ')
   endereco = input('Informe o endereco (logradouro - nro - bairro - cidade/sigla estado): ')

   cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

   clientes.append(cliente)

   print('\n***** Conta criada com sucesso ! *****')

def criar_conta(numero_conta, clientes, contas):
   cpf = input('Informe o CPF do cliente: ')
   cliente = filtrar_cliente(cpf, clientes)

   if not cliente:
      print('\n+++ Cliente nao cadastrado! Fluxo de criacao de conta encerrado! +++')
      return
   
   conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
   contas.append(conta)
   cliente.contas.append(conta)

   print('\n***** Conta criada com sucesso ! *****')

def listar_contas(contas):
   for conta in contas:
      print('+' * 50)
      print(textwrap.dedent(str(conta)))



def main():
   clientes = []
   contas = []

   while True:
      opcao = menu()

      if opcao == 'd':
         depositar(clientes)

      elif opcao == 's':
         sacar(clientes)

      elif opcao == 'e':
         exibir_extrato(clientes)
      
      elif opcao == 'nu':
         criar_clientes(clientes)

      elif opcao == 'nc':
         numero_conta = len(contas) + 1
         criar_conta(numero_conta, clientes, contas)


      elif opcao == 'lc':
         listar_contas(contas)

      elif opcao == 'q':
         break

      else:
         print('\n+++ Operacao invalida, pro favor selecione novamente a operacao desejada! +++')


main()