import requests
import pandas as pd
import sqlite3

BASE_URL = "https://pokeapi.co/api/v2/pokemon"
LIMIT = 151
DATABASE_FILE = "pokemon_gen1.db"
TABLE_NAME = "pokemon"

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

df["total_stats"] = (
    df["hp"]
    + df["attack"]
    + df["defense"]
    + df["special_attack"]
    + df["special_defense"]
    + df["speed"]
)

connection = sqlite3.connect(DATABASE_FILE)

df.to_sql(TABLE_NAME, connection, if_exists="replace", index=False)

top_5_total_stats_query = """
SELECT name, total_stats, first_type, second_type
FROM pokemon
ORDER BY total_stats DESC
LIMIT 5
"""

top_5_total_stats = pd.read_sql(top_5_total_stats_query, connection)

print("Data saved successfully to SQLite database.")
print(f"Database file: {DATABASE_FILE}")
print(f"Table name: {TABLE_NAME}")
print("\nTop 5 Pokemon by total stats:")
print(top_5_total_stats.to_string(index=False))

connection.close()