from fastapi import FastAPI

# models
from app.services.db_insert import insert

# database
from app.database.db_session import create_tables

app = FastAPI()

""" create_tables()

insert('Picachu', 'Eletrico')
insert('Natu', 'Voador')
insert('Monkey', 'Fogo')
insert('Miua', None) """

from app.routes import pokemon
