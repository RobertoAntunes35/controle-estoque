from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, SmallInteger
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

# docker run --name db-postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=123456 -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
from dotenv import dotenv_values

# Conexão
modeloPOSTGRESQL = 'postgresql://{usuario}:{senha}@{localhost}/{nomebanco}'


env_vars = dotenv_values()
modeloMYSQL = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'.format(
    user = env_vars['MYSQL_USER'],
    password = env_vars['MYSQL_PASSWORD'],
    host = env_vars['MYSQL_HOST'],
    port = env_vars['MYSQL_PORT'],
    database = env_vars['MYSQL_DATABASE']
)

engine = create_engine(modeloMYSQL)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

class Fornecedores(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key = True)
    codigo = Column(Integer)
    descricao = Column(String)

class Vendedores(Base):
    __tablename__ = 'vendedores'
    id = Column(Integer, primary_key = True)
    codigo = Column(Integer)
    nome = Column(String)

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key = True)
    codigo = Column(Integer)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    cidade = Column(String)
    vendedor_responsavel = Column(String)
    dia_visita = Column(Integer)

class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True)
    codigo = Column(Integer)
    descricao = Column(String)
    codigo_fornecedor = Column(Integer)
    valor_custo = Column(Float)
    comissao = Column(Float)
    unidade = Column(String)
    controle = Column(Boolean)

class Estoque(Base):
    __tablename__ = 'estoque'
    id = Column(Integer, primary_key = True)
    codigo = Column(Integer)
    descricao = Column(String)
    quantidade = Column(Integer)
    lote = Column(String)
    data_registro = Column(DateTime)
    data_vencimento = Column(DateTime)
    tipo_entrada = Column(String)

class Tabela(Base):
    __tablename__='tabela'
    id = Column(SmallInteger, primary_key = True)
    nome = Column(String(45))
    sobrenome = Column(String(45))

    def __str__(self):
        return f'Nome: {self.nome} Sobrenome: {self.sobrenome}'

result = session.query(Tabela).all()

for i in result:
    print(i)