import os 
import sys 

from flask import Flask, render_template

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'Libs'))

app = Flask(__name__)

import apps
from config import *
from Databases import Base, engine
import modelsSQL as mysql

Base.metadata.create_all(engine)

clientes = apps.Excel('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
produtos = apps.Excel('\%s' % FILES[0]['FILE_PRODUTOS'][0], **FILES[0]['FILE_PRODUTOS'][1])
fornecedores = apps.Excel('\%s' % FILES[0]['FILE_FORNECEDORES'][0], **FILES[0]['FILE_FORNECEDORES'][1])
vendedores = apps.Excel('\%s' % FILES[0]['FILE_VENDEDORES'][0], **FILES[0]['FILE_VENDEDORES'][1])

# Para a inclusão de fornecedores teremos:
crudFornecedor = apps.FornecedoresCRUD(mysql.Fornecedores)
crudCliente = apps.ClientesCRUD(mysql.Clientes)
crudProduto = apps.ProdutosCRUD(mysql.Produtos)
crudVendedores = apps.VendedoresCRUD(mysql.Vendedores)
crudEstoqueProvisorio = apps.EstoqueProvisorio(mysql.EstoqueProvisorio)


# Inserções e Verificações
# Pensar em uma função assincrona
for codigo, descricao in zip(fornecedores.newArray[0], fornecedores.newArray[1]):
    crudFornecedor.createFornecedor(codigo, descricao)

for codigo, razao_social, nome_fantasia, cidade, dia_visita, vendedor_responsavel in zip(clientes.newArray[0],clientes.newArray[1],clientes.newArray[2],clientes.newArray[3],clientes.newArray[4],clientes.newArray[5]):
    crudCliente.createCliente(codigo, razao_social, nome_fantasia, cidade, vendedor_responsavel,dia_visita)

for codigo, descricao, unidade, valor_custo, codigo_fornecedor, controle, comissao, codigo_completo in zip(produtos.newArray[0],produtos.newArray[1], produtos.newArray[2], produtos.newArray[3], produtos.newArray[4], produtos.newArray[5], produtos.newArray[6], produtos.newArray[7]):
    crudProduto.createProduto(codigo, codigo_completo, descricao, codigo_fornecedor, valor_custo, comissao, unidade, controle)

for codigo, nome in zip(vendedores.newArray[0], vendedores.newArray[1]):
    crudVendedores.createVendedor(codigo, nome)



# Consultas
# crudFornecedor.read()
# crudCliente.read()
# crudProduto.read()
# crudVendedores.read()


@app.route('/teste/<item_id>')
def exibir_item(item_id):
    item = crudEstoqueProvisorio.read()
    print(item)

    return render_template('pedidos.html', item = item)

@app.route("/teste")
def index():
    return render_template('pedidos.html')

Pedido = {
    'id':'37243',
    'cliente':{
        'CodigoCliente':1,
        'Endereco':'AV 29, 693 FUNDOS',
        'Cidade':'Rio Claro'
    },
    'codigo_vendedor':10,
    'tipo_pagamento':'A vista',
    'itens': {
        'item1': {
            'descricao':'ACQUISSIMA 1,5L S/ GAS C/06 UN',
            'quantidade':10,
            'valor_unidade':1.5,
            'valor_total':'valor_unidade x quantidade'
        }
    }
}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)