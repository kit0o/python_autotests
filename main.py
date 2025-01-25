import requests
import json

#Автотесты на сайт pokemonbattle.ru

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f0c951500b4c39b6947f1e21dd16bc6'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token': TOKEN}
body_create_a_pokemon = {
    "name": "generate",
    "photo_id": -1
}
# Создание покемона v
responseCreate = requests.post(url = f'{URL}/pokemons', headers= HEADER, json=body_create_a_pokemon)
print(responseCreate.text)
pokemon_id = responseCreate.json()['id']

# Получение фото покемона (чтобы не менять) и имени (чтобы посмотреть, что имзенилось потом) v
responseGet = requests.get(url = f'{URL}/pokemons?pokemon_id='+ pokemon_id, headers= HEADER)
items = json.loads(responseGet.text)
photo_id = responseGet.json()['data'][0]['photo_id']
pokemon_name = responseGet.json()['data'][0]['name']
print(photo_id)
print(pokemon_name)



# Смена имени покемона v
body_change_a_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": photo_id
}
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json= body_change_a_pokemon)

# Добавить покемона в покебол v
body_add_pokeball = {
    "pokemon_id": pokemon_id
}
responseAddPokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(responseAddPokeball.text)
 