import os 
import sys 

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'Libs'))

import apps as ap 
from config import *

print(path)
clientes = ap.Excel('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
print(clientes)

