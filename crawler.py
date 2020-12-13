import requests

URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print(res.text)
        else:
            print("Status code error.")
    except Exception as err:
        print("Erro ao fazer requisição de busca.")
        print(err)

buscar(URL_AUTOMOVEIS)