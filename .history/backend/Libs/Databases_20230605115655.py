
# docker run --name db-postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=123456 -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
from dotenv import dotenv_values

# Conexão MYSQL
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, SmallInteger
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
modeloPOSTGRESQL = 'postgresql://{usuario}:{senha}@{localhost}/{nomebanco}'

env_vars = dotenv_values()
modeloMYSQL = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'.format(
    user = env_vars['MYSQL_USER'],
    password = env_vars['MYSQL_PASSWORD'],
    host = env_vars['MYSQL_HOST'],
    port = env_vars['MYSQL_PORT'],
    database = env_vars['MYSQL_DATABASE']
)

engine = create_engine(modeloMYSQL)
Session = sessionmaker(bind = engine)
Base = declarative_base()

# Conexão MONGODB
from pymongo import MongoClient

# Crie um cliente MongoDB
client = MongoClient("mongodb://localhost:27017/")


db = client[env_vars['MONGO_DATABASE']]


collection = db['orders']
Pedido = {
    'ClienteCode':1,
    'cliente':'Balcao',
    'products':{
        'firstProduct':{
            'name':'Abc',
            'Quantidade':10,
            'valorVenda':15.00,
            'valorTotal': 150.00
        },
    }
}

collection.insert_one(Pedido)
