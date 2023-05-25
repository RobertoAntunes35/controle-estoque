import pandas as pd 
import numpy as np 

from config import *

class ConversionExcel:
    def __init__(self, filename, **columns) -> None:
        
        if filename.rsplit('.')[1] not in EXTENSION: 
            raise TypeError('Não há suporte para a extensão: %s ' % filename.rsplit('.')[1])    
        try:
            self.fileExcel = pd.read_excel(path + filename).rename(columns=columns)

        except Exception as error:
            print(type(error).__name__)

    def matrizDados(self):
        pass


for i in FILES[0]:
    print(i)
print(FILES[0]['FILE_CLIENTES'])