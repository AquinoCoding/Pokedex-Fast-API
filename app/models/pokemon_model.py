import sqlalchemy as sa

from datetime import datetime

from .model_base import ModelBaseSQL

class Pokemon(ModelBaseSQL):
    __tablename__: str = 'pokemon'
    
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    data_modificacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    name: str = sa.Column(sa.String(45), nullable=False)
    type_pokemon: str = sa.Column(sa.String(45), nullable=False)

    def __repr__(self) -> str:
        return f'<Pokemon>'