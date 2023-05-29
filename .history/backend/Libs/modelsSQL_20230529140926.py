from sqlalchemy import Integer, SmallInteger, String, Float, DateTime, Boolean,Column
from Databases import Base

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
    codigo_completo = Column(Integer)
    descricao = Column(String(150))
    codigo_fornecedor = Column(Integer)
    valor_custo = Column(Float)
    comissao = Column(Float)
    unidade = Column(String(150))
    controle = Column(Boolean)

    def __repr__(self):
        return f'Id: {self.id} Código: {self.codigo} Descrição: {self.descricao}'

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

class EstoqueProvisorio(Base):
    __tablename__ = 'estoqueProvisorio'
    id = Column(SmallInteger, primary_key = True, autoincrement = True)
    codigo = Column(Integer, autoincrement = True)
    descricao = Column(String(350))
    data_vencimento = Column(DateTime)
    quantidade = Column(Integer)







class Tabela(Base):
    __tablename__='tabela'
    id = Column(SmallInteger, primary_key = True, autoincrement = True)
    nome = Column(String(45))
    sobrenome = Column(String(45))