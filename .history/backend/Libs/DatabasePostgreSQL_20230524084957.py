from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexão
modelo = 'postgresql://{usuario}:{senha}@{localhost}/{nomebanco}'
engine = create_engine('postgresql://{usuario}:{senha}@{localhost}/{nomebanco}')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

