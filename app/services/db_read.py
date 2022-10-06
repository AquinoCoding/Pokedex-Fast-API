# models
from app.models.pokemon_model import Pokemon

# db
from app.database.db_session import create_session

def read():
    with create_session() as session:
        item: Pokemon = session.query(Pokemon)
        
        response = [{"id": an.id, "name": an.name, 
                        "type_pokemon": an.type_pokemon, 
                        "creat_date": an.creat_date,
                        "data_modificacao": an.data_modificacao} 
                            
                            for an in item]
        
        return response

def read_filter(type_pokemon: str):

    with create_session() as session:
        item: Pokemon = session.query(Pokemon)
        
        response = [{"id": an.id, "name": an.name, 
                        "type_pokemon": an.type_pokemon, 
                        "creat_date": an.creat_date,
                        "data_modificacao": an.data_modificacao} 
                         
                         for an in item if type_pokemon in an.type_pokemon.split(';')]

        return response

def read_single(id_: str):
    with create_session() as session:
        item: Pokemon = session.query(Pokemon).filter(Pokemon.id == id_).one_or_none()
    
    return item
