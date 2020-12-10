import json

import requests

#Documentação API : https://restcountries.eu/
URL = "https://restcountries.eu/rest/v2/all"

res = requests.get(URL)

paises = json.loads(res.text)

for pais in paises:
    print(pais['name'])
print(len(paises))