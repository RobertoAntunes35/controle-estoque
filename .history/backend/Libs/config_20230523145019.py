import os 
import sys 

STATIC_FILE = '\..\static_file'

EXTENSION = {
    'xls','xlsx','csv','xlsm'
}

FILES = {
'FILE_CLIENTE':'D01_Cliente.xls',
'FILE_PRODUTOS':'\D04_Produto_Completo.xls',
'FILE_FORNECEDOR':'\D08Fornecedor:xls',
'FILE_VENDEDOR':'\D20_Vendedor.xls',
'FILE_PEDIDO_ITENS':'\Pedidos.Itens.xls',
'FILE_PEDIDOS':'\Pedidos.xls'
}

path = os.path.dirname(os.path.abspath(sys.argv[0])) + STATIC_FILE
