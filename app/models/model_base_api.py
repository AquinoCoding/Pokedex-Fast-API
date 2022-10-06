from pydantic import BaseModel
from typing import Optional


class PokemonBase(BaseModel):
    name: str
    type_pokemon: Optional[str] = None
        