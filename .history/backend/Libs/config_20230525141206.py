import os 
import sys 

STATIC_FILE = '\..\static_file'

EXTENSION = {
    'xls','xlsx','csv','xlsm'
}

FILES = [
    {
        'FILE_FORNECEDORES': [
            'D08_Fornecedor.xls',
            {
                'D01_Cod_Cliente':'codigo_fornecedor',
                'D01_Fantasia':'nome_fornecedor',
            }
        ],
        'FILE_VENDEDORES':[
            'D20_Vendedor.xls',
            {
                'D03_Salao':'codigo_vendedor',
                'D03_Descricao':'nome_vendedor',
            }
        ],
        'FILE_CLIENTES':[
            'D01_Cliente.xls',
            {
                '01_Cod_Cliente':'codigo_cliente',
                'D01_Nome':'razao_cliente',
                'Fantasia':'nome_cliente',
                'D01_Cidade':'cidade_cliente',
                'xregiao':'dia_visita_cliente',
                'D01_Vendedor':'vendedor_cliente',
            }
        ],
        'FILE_PRODUTOS':[
            'D04_Produto_Completo.xls',
            {
                'D04_Cod':'codigo_produto',
                'D04_Descricao':'descricao_produto',
                'D04_UniPro':'unidade_produto',
                'D04_Precom':'valor_custo_produto',
                'Combinação47':'codigo_fornecedor',
                'Controle':'controle',
                'Comissao':'comissao',
            }
        ],
        'FILES_PEDIDOS':[
            {
                'PEDIDO_ITENS':[
                    'Pedidos_Itens.xls',
                    {
                        'Numero':'codigo_pedido',
                        'QUANT':'quantidade',
                        'Texto28':'item',
                        'Texto29':'codigo_produto_completo',
                        'Vl_Prod':'valor_venda',
                        'Texto37':'unidade',
                        'Texto68':'codigo_produto'
                    }
                ],
                'PEDIDO':[
                    'Pedido.xls',
                    {
                        'Texto14':'nome_cliente',
                        'CODCLI':'codigo_cliente',
                        'Numero':'codigo_pedido',
                        'VALPED':'valor_total',
                        'Texto36':'tipo_operacao',
                        'Data_Importacao':'data_importacao',
                        'xvencimento':'metodo_pagamento',
                    }
                ]
            }
        ]
    }
]

path = os.path.dirname(os.path.abspath(__file__)) + STATIC_FILE