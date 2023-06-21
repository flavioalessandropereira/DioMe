"""
    Desafio de projeto utilizando o Alchemry
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, select, func
from sqlalchemy import inspect
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    # atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9), nullable=False)
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Conta(id={self.id}, nome ={self.nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo_conta = Column(String)
    agencia = Column(String)
    numero_conta = Column(Integer, nullable=False)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta (id={self.id}, tipo_conta={self.tipo_conta}, agencia={self.agencia}, " \
               f"numero_conta={self.numero_conta})"


print(Cliente.__tablename__)
print(Conta.__tablename__)

# conexao com banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


#
with Session(engine) as session:
    flavio = Cliente(
        nome = 'flavio',
        cpf = '111111111',
        endereco = 'Rua José Aqui'
    )
    felipe = Cliente(
        nome='felipe',
        cpf='333333333',
        endereco='Rua Aqui'
    )
#
    tamara = Cliente(
        nome='tamara',
        cpf='222222222',
        endereco='Aqui em casa'
    )
#
    #enviando para o BD (persistencia de dados)
    session.add_all([flavio, felipe, tamara])
#
#     session.commit()
#
stmt = select(Cliente).where(Cliente.nome.in_(["flavio", "tamara"]))
print('Recuperando usuarios a partir de condicao de filtragem')
for cliente in session.scalars(stmt):
    print(cliente)

stmt_conta = select(Conta).where(Conta.cliente_id.in_([2]))
for conta in session.scalars(stmt_conta):
    print(conta)



stmt_order = select(Cliente).order_by(Cliente.nome.desc())
print("\nRecuperando info de maneira ordenada descendente")
for result in session.scalars(stmt_order):
    print(result)

stmt_count = select(func.count('*')).select_from(Cliente)
print('Total de instancias em Cliente')
for result in session.scalars(stmt_count):
    print(result)
