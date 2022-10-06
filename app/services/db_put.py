# libs
from datetime import datetime

# models
from app.models.pokemon_model import Pokemon

# db
from app.database.db_session import create_session

def edit(id_: str, name: str, type_pokemon: str):
    
    with create_session() as session:
        itens: Pokemon = session.query(Pokemon).filter(Pokemon.id == id_).one_or_none()
        
        if itens:
            itens.name = name
            itens.data_modificacao = datetime.now()
            itens.type_pokemon = type_pokemon

            session.commit()
            
            return True
        
        
        return False