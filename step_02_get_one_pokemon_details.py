import requests

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/4/"

response = requests.get(POKEMON_URL)
response.raise_for_status()

pokemon_data = response.json()

name = pokemon_data['name'].capitalize()
height= pokemon_data["height"]
weight = pokemon_data["weight"]
first_type = pokemon_data["types"][0]["type"]["name"].capitalize()

print("Name:", name)
print("Height:", height)
print("Weight:", weight)

if len(pokemon_data["types"]) > 1:
    print("First type:", first_type)
    second_type = pokemon_data["types"][1]["type"]["name"].capitalize()
    print("Second type:", second_type)
else:
    print("Type:", first_type)
