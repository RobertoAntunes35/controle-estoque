import pandas as pd 
import numpy as np 
import logging


from sqlalchemy.exc import SQLAlchemyError

from config import *

import DatabasePostgreSQL as mysql

class Excel:
    def __init__(self, filename, **columns) -> None:
        self.Session = mysql.Session()
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




class CRUD:
    def __init__(self, db) -> None:
        self.db = db 
    def handle_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except SQLAlchemyError as e:
                print('Ocorreu um erro no SQLAlchemy: %s' % str(e))
        return wrapper

class ClientesCRUD:
    def __init__(self,):
        pass 

class ProdutosCRUD:
    def __init__(self) -> None:
        pass

class FornecedoresCRUD:
    def __init__(self) -> None:
        self.session = mysql.Session()
    
    def createFornecedor(self, codigo, descricao):
        # Primeiro passo para a consulta
        # Consultar se o fornecedor já existe no banco
        
        fornecedor = mysql.Fornecedores(
            id = None,
            codigo = codigo,
            descricao = descricao
        )   
        self.session.add(fornecedor)
        self.session.commit()
        print('Sucessfull about to insert the new Fonecedor with %s %s' % (codigo, descricao))


class VendedoresCRUD:
    def __init__(self) -> None:
        pass

class PedidosCRUD:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    # from DatabasePostgreSQL import *

    mysql.Base.metadata.create_all(mysql.engine)
    

    clientes = Excel('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
    produtos = Excel('\%s' % FILES[0]['FILE_PRODUTOS'][0], **FILES[0]['FILE_PRODUTOS'][1])
    fornecedores = Excel('\%s' % FILES[0]['FILE_FORNECEDORES'][0], **FILES[0]['FILE_FORNECEDORES'][1])
    vendedores = Excel('\%s' % FILES[0]['FILE_VENDEDORES'][0], **FILES[0]['FILE_VENDEDORES'][1])

    crud_Fornecedor = FornecedoresCRUD()

    crud_Fornecedor.createFornecedor('', 10, 'BELLPAR')


    

