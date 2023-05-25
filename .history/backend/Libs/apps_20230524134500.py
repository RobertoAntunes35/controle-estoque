import pandas as pd 
import numpy as np 
import logging

from config import *
from DatabasePostgreSQL import Session
import DatabasePostgreSQL as postgre

from sqlalchemy.exc import SQLAlchemyError

class Excel:
    def __init__(self, filename, **columns) -> None:
        self.Session = Session()
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

    def dropColumns(self) -> pd.DataFrame:
        columnsSelect = self.columns.values()
        columnsDrop = []
        for column in self.fileExcel.columns:
            if column not in columnsSelect:
                columnsDrop.append(column)
        newDataFrame = self.fileExcel.drop(columnsDrop, axis = 1)
        return newDataFrame
    
    def dataFrameToArray(self, frame) -> np.array:
        newArray = np.array(frame)
        return newArray.T


def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            print('Ocorreu um erro no SQLAlchemy: %s' % str(e))
        return wrapper

class CRUD:
    def __init__(self, db) -> None:
        self.db = db 


class ClientesCRUD(Excel):
    def __init__(self, filename, **columns) -> None:
        super().__init__(filename, **columns)



class ProdutosCRUD:
    def __init__(self) -> None:
        pass

class FornecedoresCRUD(CRUD):
    def __init__(self, db) -> None:
        super().__init__(db)
    
    def create(self, codigo, descricao):
        fornecedor = postgre.Fornecedores(
            codigo = codigo,
            descricao = descricao
        ) 


class VendedoresCRUD:
    def __init__(self) -> None:
        pass

class PedidosCRUD:
    def __init__(self) -> None:
        pass




    
            


if __name__ == '__main__':
    # from DatabasePostgreSQL import *

    # Base.metadata.create_all(engine)
    

    clientes = Clientes('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
    produtos = Produtos('\%s' % FILES[0]['FILE_PRODUTOS'][0], **FILES[0]['FILE_PRODUTOS'][1])
    fornecedores = Fornecedores('\%s' % FILES[0]['FILE_FORNECEDORES'][0], **FILES[0]['FILE_FORNECEDORES'][1])
    vendedores = Vendedores('\%s' % FILES[0]['FILE_VENDEDORES'][0], **FILES[0]['FILE_VENDEDORES'][1])

    dictTeste = {
        'Nome':'nome',
        'Idade':'idade',
        'Cidade':'cidade'
    }

    crud = CRUD('abc')
    crud.insertValue('Clientes', 'Lucas', 12, 'Ipeuna', **dictTeste)

