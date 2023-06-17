from abc import ABC, abstractclassmethod, abstractmethod
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
    pass
    

class Historico:
    pass
    

class Transacao(ABC):
    pass
    

class Saque(Transacao):
    pass # continuidade ...


class Deposito(Transacao):
    pass

      
