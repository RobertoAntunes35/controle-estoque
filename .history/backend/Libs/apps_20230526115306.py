import pandas as pd 
import numpy as np 
import logging

from sqlalchemy.exc import SQLAlchemyError

from config import *
import modelsSQL as mysql
from Databases import Session, engine, Base


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

    def __repr__(self) -> str:
        return 'Ok'
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
    def __init__(self, table) -> None:
        self.session = Session()
        self.table = table
    
    def handle_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except SQLAlchemyError as e:
                print('Ocorreu um erro no SQLAlchemy: %s' % str(e))
        return wrapper
    
    @handle_error
    def read(self, *args):
        if args:
            for i, arg in enumerate(args):
                result = self.session.query(self.table).filter_by(self.table.codigo == arg).first()
                if not result:
                    print(f'O valor {arg} não está contido no banco!')
                    continue
                print(result)
    
        else:
            result = self.session.query(self.table).all()
            for row in result:
                print(row)
    
    def update(self, id, **kwargs):
        '''Para atualizar um valor, você precisará de um dicionário, que contenha a COLUNA  seguida do VALOR'''
        if not id:
            raise ValueError('Você precisa selecionar um ID para alterar o valor.')
        self.session.query(self.table).filter_by(id = id).update(kwargs)
        self.session.commit()
        print('Alteração Executada com sucesso.')

class ClientesCRUD(CRUD):
    def __init__(self) -> None:
        super().__init__() 

class ProdutosCRUD(CRUD):
    def __init__(self) -> None:
        super().__init__()

    def handle_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except SQLAlchemyError as e:
                print('Ocorreu um erro no SQLAchemy: %s' % str(e))
            return (wrapper)

    @handle_error
    def createProduto(self, codigo, codigo_produto_completo, descricao, codigo_fornecedor, valor_custo, comissao, unidade, controle):
        # Primeiro, procurar pelo produto:
        result = self.session.query(mysql.Produtos).filter_by(codigo_produto_completo).first()
        if result:
            print('O produto %s já existe no banco.' % descricao)
        else:
            objetoProduto = mysql.Produtos(
                id=None,
                codigo=int(codigo),
                codigo_completo=int(codigo_produto_completo),
                descricao=str(descricao),
                codigo_fornecedor=int(codigo_fornecedor),
                valor_custo=float(valor_custo),
                comissao=float(comissao),
                unidade=str(unidade),
                controle=bool(controle)
            )
            self.session.add(objetoProduto)
            self.session.commit()
            print('Sucessfull about to insert the new Produto with %s %s' % (codigo, descricao))

class FornecedoresCRUD(CRUD):
    def __init__(self, table) -> None:
        super().__init__(table)
        self.table = table
    
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
        
        result = self.session.query(self.table).filter_by(codigo = codigo).first()
        
        if result:
            print('O valor %s já existe no banco.' % descricao)
        
        else:
            objetoFornecedor = self.table(
                id = None,
                codigo = codigo,
                descricao = descricao
            )   
            self.session.add(objetoFornecedor)
            self.session.commit()
            print('Sucessfull about to insert the new Fonecedor with %s %s' % (codigo, descricao))

class VendedoresCRUD(CRUD):
    def __init__(self) -> None:
        super().__init__()


class PedidosCRUD(CRUD):
    def __init__(self, table) -> None:
        super().__init__(table)
        

if __name__ == '__main__':

    Base.metadata.create_all(engine)
    
    clientes = Excel('\%s' % FILES[0]['FILE_CLIENTES'][0],**FILES[0]['FILE_CLIENTES'][1])
    produtos = Excel('\%s' % FILES[0]['FILE_PRODUTOS'][0], **FILES[0]['FILE_PRODUTOS'][1])
    fornecedores = Excel('\%s' % FILES[0]['FILE_FORNECEDORES'][0], **FILES[0]['FILE_FORNECEDORES'][1])
    vendedores = Excel('\%s' % FILES[0]['FILE_VENDEDORES'][0], **FILES[0]['FILE_VENDEDORES'][1])

    crud_Fornecedor = FornecedoresCRUD(mysql.Fornecedores)



    

