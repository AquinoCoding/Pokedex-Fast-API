# sqlalchemy
import sqlalchemy as sa

# sql-orm - session
from sqlalchemy.orm import sessionmaker

# libs
from pathlib import Path
import pymysql

# sql-orm
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

# models
from app.models.model_base import ModelBaseSQL

__engine = None


def create_engine(sqlite: bool = True):
    global __engine
    
    if __engine:
        return
    
    arquivo_db = 'db/pokemon.sqlite'
    folder = Path(arquivo_db).parent
    folder.mkdir(parents=True, exist_ok=True)
    
    conn_str = f'sqlite:///{arquivo_db}'
    __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    
    return __engine
        
def create_session():
    global __engine
    
    if not __engine:
        create_engine(sqlite=True) 
        
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()
    
    return session

def create_tables():

    print('--DB in execution or reload--')

    global __engine 
    
    if not __engine:
        create_engine(sqlite=True)
        
    import app.models.__all_models
    ModelBaseSQL.metadata.drop_all(__engine)
    ModelBaseSQL.metadata.create_all(__engine)
    
