from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexão
modelo = 'postgresql://{usuario}:{senha}@{localhost}/{nomebanco}'
engine = create_engine('postgresql://{usuario}:{senha}@{localhost}/{nomebanco}')
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

