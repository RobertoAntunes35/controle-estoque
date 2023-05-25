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
Base = declarative_base()

class Fornecedores(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key = True, autoincrement = True)
    codigo = Column(Integer)
    descricao = Column(String(150))
    
    def __repr__(self):
        return f'<Id: {self.id} Código {self.codigo} Descrição: {self.descricao}>'

class Vendedores(Base):
    __tablename__ = 'vendedores'
    id = Column(Integer, primary_key = True, autoincrement = True)
    codigo = Column(Integer)
    nome = Column(String(150))

    def __repr__(self):
        return f'Id: {self.id} Código: {self.codigo} Nome: {self.nome}'

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key = True, autoincrement = True)
    codigo = Column(Integer)
    razao_social = Column(String(150))
    nome_fantasia = Column(String(150))
    cidade = Column(String(150))
    vendedor_responsavel = Column(String(150))
    dia_visita = Column(Integer)

    def __repr__(self):
        return f'Id: {self.id} Código: {self.codigo} Nome Fantasia: {self.nome_fantasia}'

class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True, autoincrement = True)
    codigo = Column(Integer)
    descricao = Column(String(150))
    codigo_fornecedor = Column(Integer)
    valor_custo = Column(Float)
    comissao = Column(Float)
    unidade = Column(String(150))
    controle = Column(Boolean)

class Estoque(Base):
    __tablename__ = 'estoque'
    id = Column(Integer, primary_key = True, autoincrement = True)
    codigo = Column(Integer)
    descricao = Column(String(150))
    quantidade = Column(Integer)
    lote = Column(String(150))
    data_registro = Column(DateTime)
    data_vencimento = Column(DateTime)
    tipo_entrada = Column(String(150))

class Tabela(Base):
    __tablename__='tabela'
    id = Column(SmallInteger, primary_key = True, autoincrement = True)
    nome = Column(String(45))
    sobrenome = Column(String(45))

