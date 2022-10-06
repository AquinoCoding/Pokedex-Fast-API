# models
from app.models.pokemon_model import Pokemon

# db
from app.database.db_session import create_session


def delete(id_: str):
    
    with create_session() as session:
        item: Pokemon = session.query(Pokemon).filter(Pokemon.id == id_).one_or_none()
        
        if item:
            session.delete(item)
            session.commit()
            
            return True
        
        return False
