import pandas as pd 
import numpy as np 

from config import *

class Excel:
    def __init__(self, filename, **columns) -> None:
        self.columns = columns 
        
        if filename.rsplit('.')[1] not in EXTENSION: 
            raise TypeError('Não há suporte para a extensão: %s ' % filename.rsplit('.')[1])    
        try:
            self.fileExcel = pd.read_excel(path + filename).rename(columns=columns)
            self.newDataFrame = self.dropColumns()
            print('Importação e alteração das colunas realizada com sucesso.')
            self.newArray = self.dataFrameToArray(self.newDataFrame)
        except Exception as error:
            print(type(error).__name__)

    def dropColumns(self):
        columnsSelect = self.columns.values()
        columnsDrop = []
        for column in self.fileExcel.columns:
            if column not in columnsSelect:
                columnsDrop.append(column)
        newDataFrame = self.fileExcel.drop(columnsDrop, axis = 1)
        return newDataFrame
    
    def dataFrameToArray(self, frame) -> np.array:
        newArray = np.array(frame).T
        return newArray

class Clientes(Excel):
    def __init__(self, filename, **columns) -> None:
        super().__init__(filename, **columns)

class Produtos(Excel):
    def __init__(self, filename, **columns) -> None:
        super().__init__(filename, **columns)

class Fornecedores(Excel):
    def __init__(self, filename, **columns) -> None:
        super().__init__(filename, **columns)

class Vendedores(Excel):
    def __init__(self, filename, **columns) -> None:
        super().__init__(filename, **columns)

class Pedidos(Excel):
    def __init__(self, filename, **columns) -> None:
        super().__init__(filename, **columns)



arquivo = Excel('\%s' % FILES[0]['FILE_CLIENTES'][0], **FILES[0]['FILE_CLIENTES'][1])
print(arquivo.newArray)



print(arquivo.newDataFrame)