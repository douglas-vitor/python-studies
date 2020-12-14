import requests

from bs4 import BeautifulSoup


DOMINIO = "https://django-anuncios.solyd.com.br"
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


def encontrar_links(soup):
    cards_pai = soup.find("div", class_="ui three doubling link cards")
    cards = cards_pai.find_all("a")
    links = []
    for card in cards:
        link = card['href']
        links.append(link)
    return links


resposta = buscar(URL_AUTOMOVEIS)
if resposta:
    soup = parsing(resposta)
    if soup:
        links = encontrar_links(soup)
        for link in links:
            print(link)