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
    

    def handle_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except SQLAlchemyError as e:
                print('Ocorreu um erro no SQLAlchemy: %s' % str(e))
        return wrapper
    
    @handle_error
    def createFornecedor(self, codigo, descricao):
        # Consultar se o fornecedor já existe no banco
        # Primeiro passo para a consulta
        result = self.session.query(mysql.Fornecedores).filter_by(codigo = codigo).first()


        if result:
            raise ValueError('O valor %s já existe no banco.')
        
        objetoFornecedor = mysql.Fornecedores(
            id = None,
            codigo = codigo,
            descricao = descricao
        )   
        self.session.add(objetoFornecedor)
        self.session.commit()
        print('Sucessfull about to insert the new Fonecedor with %s %s' % (codigo, descricao))

    @handle_error
    def readFornecedor(self, *args):
        '''For to choice a specific vale, you can to put one or more values to COLUMN codigo '''
        if args:
            for i, arg in enumerate(args):
                
                result = self.session.query(mysql.Fornecedores).filter(mysql.Fornecedores.codigo == arg).first()
                if not result:
                    print(f'O valor {arg} não está contido no banco')
                    continue
                print(result)
                
        else:
            result = self.session.query(mysql.Fornecedores).all()
            for row in result:
                print(row)

    @handle_error
    def updateFornecedor(self, id, **kwargs):
        '''Para atualizar um valor, você precisará de um dicionário, que contenha a COLUNA  seguida do VALOR'''
        if not id:
            raise ValueError('Você precisa selecionar os IDS para alterar os valores')
        self.session.query(mysql.Fornecedores).filter_by(id = id).update(kwargs)
        self.session.commit()
        print('Alteração executada com sucesso.')

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

    # crud_Fornecedor.createFornecedor(11, 'BELLPAR')

    crud_Fornecedor.readFornecedor(10,13,11)
    crud_Fornecedor.updateFornecedor(1, **{
        'adaa':13
    })


    

