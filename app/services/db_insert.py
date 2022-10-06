# models
from app.models.pokemon_model import Pokemon

# db
from app.database.db_session import create_session

def insert(name: str, type_pokemon: str):
    
    itens: Pokemon = Pokemon(name=name, type_pokemon=type_pokemon)
    
    with create_session() as session:
        session.add(itens)
        session.commit()
        