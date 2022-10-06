from main import app
from fastapi import status, HTTPException

# models
from app.models.pokemon_model import Pokemon
from app.models.model_base_api import PokemonBase

# services
from app.services.db_read import read, read_single
from app.services.db_put import edit
from app.services.db_insert import insert
from app.services.db_delete import delete


@app.get("/pokemons")
def pokemons_all():
    
    pokemons = read()
    
    return pokemons

@app.get("/pokemons/{id_pokemon}")
def pokemon(id_pokemon: int):
    
    pokemon = read_single(id_pokemon)
    
    if pokemon:
        return pokemon
    
    else:
        raise HTTPException(status_code=404, 
                            detail=f"pokemon id {id_pokemon} not found")

@app.put("/pokemons/{id_pokemon}")
def edit_pokemon(id_pokemon: int, pokemon: PokemonBase):
    
    if edit(id_pokemon, pokemon.name, pokemon.type_pokemon):
        return {'detail': 'Pokemon alterado com sucesso'}
    
    else:
        raise HTTPException(status_code=404, 
                        detail=f"pokemon id {id_pokemon} not found")

@app.post("/pokemons")
def inserir_pokemon(pokemon: PokemonBase):
    
    insert(pokemon.name, pokemon.type_pokemon)
    return pokemon

@app.delete("/pokemon/{id_pokemon}")
def delete_pokemon(id_pokemon: int):
    
    if delete(id_pokemon):
        return {'detail': 'Delete concluido com sucesso'}
    
    else:
        raise HTTPException(status_code=404, 
                            detail=f"pokemon id {id_pokemon} not found")
