import requests

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/1/"

response = requests.get(POKEMON_URL)
response.raise_for_status()

pokemon_data = response.json()

name = pokemon_data["name"].capitalize()

print("Name:", name)
print()

for stat in pokemon_data['stats']:
    stat_name = stat["stat"]["name"].replace("-", " ").title()
    base_stats = stat["base_stat"]
    print(f"{stat_name}: {base_stats}")