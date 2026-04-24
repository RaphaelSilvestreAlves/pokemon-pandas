import requests
import pandas as pd

BASE_URL = "https://pokeapi.co/api/v2/pokemon"
LIMIT = 151

response = requests.get(f"{BASE_URL}?limit={LIMIT}")
response.raise_for_status()

data = response.json()
pokemon_list = data["results"]

all_pokemon_data = []

for pokemon in pokemon_list:
    pokemon_response = requests.get(pokemon["url"])
    pokemon_response.raise_for_status()
    pokemon_data = pokemon_response.json()

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
        "id": pokemon_data["id"],
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

    all_pokemon_data.append(pokemon_info)

df = pd.DataFrame(all_pokemon_data)

fastest_pokemon = df.sort_values(by="speed", ascending=False)
strongest_physical_pokemon = df.sort_values(by="attack", ascending=False)
strongest_special_pokemon = df.sort_values(by="special_attack", ascending=False)


print("Top 5 fastest Pokemon:")
print(fastest_pokemon[["name", "speed", "first_type", "second_type"]].head(5).to_string(index=False))

print("\nTop 5 strongest physical attack Pokemon:")
print(strongest_physical_pokemon[["name", "attack", "first_type", "second_type"]].head(5).to_string(index=False))

print("\nTop 5 strongest special attack Pokemon:")
print(strongest_special_pokemon[["name", "special_attack", "first_type", "second_type"]].head(5).to_string(index=False))