import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0946d78a90094fed59bf1f766a380f6e'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "JuliaMaslennikova1997@yandex.ru",
    "password": "Iloveqa11"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Тарантино",
    "photo_id": 3
}

body2_create = {
    "pokemon_id": "131697",
    "name": "Бэлла",
    "photo_id": 2
}

body3_create = {
    "pokemon_id": "131697"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)

print(response.text)'''


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)

print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response2_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body2_create)
print(response2_create.text)

response3_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body3_create)
print(response3_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)