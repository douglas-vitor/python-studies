import requests

#Documentação API : https://restcountries.eu/

URL = "https://restcountries.eu/rest/v2/all"
res = requests.get(URL)
print(res.text)