import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'yourTokenHere'
HEADER = {'Content-Type' : 'application/json'}
TRAINER_ID = '18611'
# проверка, что статус-код приходит 200
def test_status_code():
    response_status_code = requests.get(url = f'{URL}/trainers')
    assert response_status_code.status_code == 200
# Проверка, что приходит наше имя тренера
def test_trainer_name():
    response_trainer_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer_name.json()['data'][0]['trainer_name'] == 'FishAndChips'