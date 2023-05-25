import pandas as pd 
import numpy as np 

from config import *

class ConversionExcel:
    def __init__(self, filename, **columns) -> None:
        
        if filename.rsplit('.')[1] not in EXTENSION: 
            raise TypeError('Não há suporte para a extensão: %s ' % filename.rsplit('.')[1])    
        try:
            self.fileExcel = pd.read_excel(path + filename).rename(columns=columns)
            print('Importação e alteração das colunas realizada com sucesso.')

        except Exception as error:
            print(type(error).__name__)

    def matrizDados(self):
        pass

arquivo = ConversionExcel((FILES[0]['FILE_CLIENTES'][0]), **FILES[0]['FILE_CLIENTES'][1])
print(EXTENSION)


print(FILES[0]['FILE_CLIENTES'][0].rsplit('.')[1])

print(FILES[0]['FILE_CLIENTES'][0])