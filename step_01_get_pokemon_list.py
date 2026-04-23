import requests

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'
LIMIT = 151

response = requests.get(f'{BASE_URL}?limit={LIMIT}')
response.raise_for_status()

data = response.json()

pokemon_list = data['results']

print(pokemon_list[:5])