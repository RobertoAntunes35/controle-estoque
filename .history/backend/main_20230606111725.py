import os 
import sys 
import datetime

from flask import Flask, render_template, request, jsonify

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
crudEstoque = apps.EstoqueCRUD(mysql.Estoque)

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

@app.route('/teste')
def home():
    return render_template('index.html')

@app.route('/produtos/insercao')
def insercao_estoque():
    return render_template('insercao.html')

@app.route('/pedidos/tirarPedidos')
def tirar_pedidos():
    return render_template('paginaGeracaoPedidos.html')

@app.route('/busca_produtos', methods=['GET', 'POST'])
def busca_produtos():
    codigoProduto = request.form['codigoProduto']
    produto = crudProduto.read(codigoProduto)

    if not produto:
        return jsonify({'updatedValueProduto': {
            'descricao': 'Não encontrado.',
            'valorVenda': 0,
            'unidadeProduto':'Não encontrado.'
        }})
    return jsonify({'updatedValueProduto': {
        'descricao':produto.descricao,
        'valorVenda':produto.valor_custo,
        'unidade':produto.unidade,
    }})


@app.route('/busca_clientes', methods=['GET', 'POST'])
def busca_clientes():
    codigoCliente = request.form['codigoCliente']
    cliente = crudCliente.read(codigoCliente)

    if not cliente:
        return jsonify({'updatedValueCliente': {
            'nomeFantasia': '',
            'endereco':'',
            'cidade':'',
            'dataEntrega':''
        }})
    
    return jsonify({'updatedValueCliente'})

# @app.route('/busca_produtos', methods=['GET', 'POST'])
# def busca_produtos():
#     value_codigo = request.form['codigoProduto']
#     produto = crudProduto.read(value_codigo)
    
#     if not produto:
#         return jsonify({'updatedValue': {
#             'descricao':'Não encontrado !',
#             'codigoFornecedor':'Não encontrado !',
#             'unidade':'Não encontrado !'
#         }})

#     return jsonify({'updatedValue': {
#         'descricao':produto.descricao,
#         'codigoFornecedor':produto.codigo_fornecedor,
#         'unidade':produto.unidade
#     }})

@app.route('/inserir_produto', methods = ['POST', 'GET'])
def inserir_produto():
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        codigo_fornecedor = request.form['codigoFornecedor']
        unidade = request.form['unidade']
        quantidade = request.form['quantidade']
        lote = request.form['lote']
        dataRegistro = request.form['dataRegistro']
        dataVencimento = request.form['dataVencimento']
        tipoEntrada = request.form['tipoEntrada']
        
        crudEstoque.createEstoque(codigo, descricao, codigo_fornecedor,unidade,quantidade,lote,dataRegistro, dataVencimento, tipoEntrada)
        return render_template('insercao.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)