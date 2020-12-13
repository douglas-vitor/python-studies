import requests

from bs4 import BeautifulSoup


URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        else:
            print("Status code error.")
    except Exception as err:
        print("Erro ao fazer requisição de busca.")
        print(err)


def parsing(res_html):
    try:
        soup = BeautifulSoup(res_html, "html.parser")
        return soup
    except Exception as err:
        print("Erro no parsing.")
        print(err)

resposta = buscar(URL_AUTOMOVEIS)
if resposta:
    soup = parsing(resposta)