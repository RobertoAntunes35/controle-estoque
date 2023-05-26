import os 
import sys 

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'Libs'))

import apps as app
from config import *
from Databases import Base, engine
import modelsSQL as mysql

Base.metadata.create_all(engine)

clientes = app.Excel('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
produtos = app.Excel('\%s' % FILES[0]['FILE_PRODUTOS'][0], **FILES[0]['FILE_PRODUTOS'][1])
fornecedores = app.Excel('\%s' % FILES[0]['FILE_FORNECEDORES'][0], **FILES[0]['FILE_FORNECEDORES'][1])
vendedores = app.Excel('\%s' % FILES[0]['FILE_VENDEDORES'][0], **FILES[0]['FILE_VENDEDORES'][1])

# Para a inclusão de fornecedores teremos:
crudFornecedor = app.FornecedoresCRUD(mysql.Fornecedores)
crudCliente = app.ClientesCRUD(mysql.Clientes)
crudProduto = app.ProdutosCRUD(mysql.Produtos)
crudVendedores = app.VendedoresCRUD(mysql.Vendedores)

# Inserções e Verificações
for codigo, descricao in zip(fornecedores.newArray[0], fornecedores.newArray[1]):
    crudFornecedor.createFornecedor(codigo, descricao)

for codigo, razao_social, nome_fantasia, cidade, dia_visita, vendedor_responsavel in zip(clientes.newArray[0],clientes.newArray[1],clientes.newArray[2],clientes.newArray[3],clientes.newArray[4],clientes.newArray[5]):
    crudCliente.createCliente(codigo, razao_social, nome_fantasia, cidade, vendedor_responsavel,dia_visita)

for codigo, descricao, unidade, valor_custo, codigo_fornecedor, controle, comissao, codigo_completo in zip(produtos.newArray[0],produtos.newArray[1], produtos.newArray[2], produtos.newArray[3], produtos.newArray[4], produtos.newArray[5], produtos.newArray[6], produtos.newArray[7]):
    crudProduto.createProduto(codigo, codigo_completo, descricao, codigo_fornecedor, valor_custo, comissao, unidade, controle)

for codigo, nome in zip(vendedores.newArray[0], vendedores.newArray[1]):
    crudVendedores.createVendedor(codigo, nome)

# Consultas
crudFornecedor.read()
crudCliente.read()
crudProduto.read()
crudVendedores.read()




# codigo = Column(Integer)
#     codigo_completo = Column(Integer)
#     descricao = Column(String(150))
#     codigo_fornecedor = Column(Integer)
#     valor_custo = Column(Float)
#     comissao = Column(Float)
#     unidade = Column(String(150))
#     controle = Column(Boolean)