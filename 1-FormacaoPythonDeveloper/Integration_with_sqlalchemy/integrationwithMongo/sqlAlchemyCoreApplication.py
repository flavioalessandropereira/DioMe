from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData()

#criando Tablea
user = Table(
    'user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

print('\ninfo da Tabela users')
print(user_prefs.primary_key)
print(user_prefs.constraints)

print(metadata_obj.tables)


for table in metadata_obj.sorted_tables:
    print(table)


metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_infoFlavio', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False),
)

print('\ninfo da Tabela Financial_info')
print(financial_info.primary_key)
print(financial_info.fullname)