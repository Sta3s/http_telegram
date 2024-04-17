# 
# Uzdevums: Izmantojot bibliotēku "requests" uzģenerēt Chuck Norris jokus
# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
# https://api.chucknorris.io/
# 
# 1. Izdrukā 3 nejaušus jokus no Chuck Norris
# 
# 2. Izdrukā 3 nejaušus jokus no Chuck Norris par programmēšanu
# 
import requests

for i in range(3):
    r = requests.get('https://api.chucknorris.io/jokes/random')
    R = r.json()
    print("\n", R["value"])


for i in range(3):
    r = requests.get('https://api.chucknorris.io/jokes/random?category=dev')
    R = r.json()
    print("\n", R["value"])
