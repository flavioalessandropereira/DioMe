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

class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column (String)


    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name ={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates = "address")

    def __repr__(self):
        return f"Address (id={self.id}., email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)


# conexao com banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# depreciado será removido em futuro release
# print(engine.table_names())

#investiga o esquema de banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)


with Session(engine) as session:
    flavio = User(
        name = 'flavio',
        fullname = 'Flavio Pereira',
        address = [Address(email_address='flavioapereira@gmail.com')]
    )
    felipe = User(
        name = 'felipe',
        fullname = 'Felipe Pereira',
        address = [Address(email_address='felipepereira@gmail.com'),
                   Address(email_address='felipepereira@yahoo.com.br')]
    )

    tamara = User(
        name = 'tamara',
        fullname = 'Tamara Pereira',
    )

    #enviando para o BD (persistencia de dados)
    session.add_all([flavio, felipe, tamara])

    session.commit()

stmt = select(User).where(User.name.in_(["flavio", "tamara"]))
print('Recuperando usuarios a partir de condicao de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('Recuperando os emails de felipe')
for address in session.scalars(stmt_address):
    print(address)



stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperando info de maneira ordenada descendente")
for result in session.scalars(stmt_order):
    print(result)


stmt_order = select(User).order_by(User.fullname)
print("\nRecuperando info de maneira ordenada crecente")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

#print(select(User.fullname, Address.email_address).join_from(Address, User))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()

print('Executando statement a partir da connection')
for result in results:
    print(result)


stmt_count= select(func.count('*')).select_from(User)
print('Total de instancias em User')
for result in session.scalars(stmt_count):
    print(result)