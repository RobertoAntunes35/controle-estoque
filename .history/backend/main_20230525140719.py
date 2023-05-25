import os 
import sys 

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'Libs'))

import apps as ap 
from config import *

clientes = Excel('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
produtos = Excel('\%s' % FILES[0]['FILE_PRODUTOS'][0], **FILES[0]['FILE_PRODUTOS'][1])
fornecedores = Excel('\%s' % FILES[0]['FILE_FORNECEDORES'][0], **FILES[0]['FILE_FORNECEDORES'][1])
vendedores = Excel('\%s' % FILES[0]['FILE_VENDEDORES'][0], **FILES[0]['FILE_VENDEDORES'][1])

print(clientes.newDataFrame)

