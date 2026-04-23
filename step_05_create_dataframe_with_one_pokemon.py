import requests
import pandas as pd

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/1/"

response = requests.get(POKEMON_URL)
response.raise_for_status()

pokemon_data = response.json()

name = pokemon_data["name"].capitalize()
height = pokemon_data["height"]
weight = pokemon_data["weight"]

types = pokemon_data["types"]
first_type = types[0]["type"]["name"].capitalize()
second_type = types[1]["type"]["name"].capitalize() if len(types) > 1 else None

stats = {}

for stat in pokemon_data["stats"]:
    stat_name = stat["stat"]["name"]
    base_stat = stat["base_stat"]
    stats[stat_name] = base_stat

pokemon_info = {
    "name": name,
    "height": height,
    "weight": weight,
    "first_type": first_type,
    "second_type": second_type,
    "hp": stats["hp"],
    "attack": stats["attack"],
    "defense": stats["defense"],
    "special_attack": stats["special-attack"],
    "special_defense": stats["special-defense"],
    "speed": stats["speed"]
}

df = pd.DataFrame([pokemon_info])

print(df.to_string())