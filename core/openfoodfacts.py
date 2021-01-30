import requests
from constants import CATEGORIES
from pprint import pprint

base_url = 'https://fr.openfoodfacts.org/'
categorie_url = f'{base_url}categorie/steaks-de-boeuf.json'

response = requests.request("GET", categorie_url).json()

pprint(response)