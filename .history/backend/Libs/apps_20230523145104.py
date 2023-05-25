import pandas as pd 
import numpy as np 

from config import *

class ConversionExcel:
    def __init__(self, filename, **columns) -> None:
        
        if filename.rsplit('.')[1] not in EXTENSION: 
            raise TypeError('Não há suporte para a extensão: %s ' % filename.rsplit('.')[1])    
        try:
            self.fileExcel = pd.read_excel(path + filename)
        except Exception as error:
            print(error)

    def matrizDados(self):
        pass


pd.testing