import pandas as pd 
import numpy as np 

from config import *

class ConversionExcel:
    def __init__(self, filename, **columns) -> None:
        self.columns = columns 
        
        if filename.rsplit('.')[1] not in EXTENSION: 
            raise TypeError('Não há suporte para a extensão: %s ' % filename.rsplit('.')[1])    
        try:
            self.fileExcel = pd.read_excel(path + filename).rename(columns=columns)
            print('Importação e alteração das colunas realizada com sucesso.')

        except Exception as error:
            print(type(error).__name__)
        self.dropColumns()

    def dropColumns(self):
        columnsSelect = self.columns.values()
        columnsDrop = []
        for column in self.fileExcel.columns:
            if column not in columnsSelect:
                columnsDrop.append(column)
        print(columnsDrop)
        newDataFrame = self.fileExcel.drop(columnsDrop, axis = 1)
        return self.fileExcel.drop(columnsDrop, axis=1)

arquivo = ConversionExcel('\%s' % FILES[0]['FILE_CLIENTES'][0], **FILES[0]['FILE_CLIENTES'][1])



print(arquivo.fileExcel)