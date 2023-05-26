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

# Inserção
# for codigo, descricao in zip(fornecedores.newArray[0], fornecedores.newArray[1]):
#     crudFornecedor.createFornecedor(codigo, descricao)

print(clientes.newDataFrame.columns).tolist()


# Leitura
# crudFornecedor.readFornecedor()
