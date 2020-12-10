import json

import requests

#Documentação API : https://restcountries.eu/
URL = "https://restcountries.eu/rest/v2/all"
URL_NAME = "https://restcountries.eu/rest/v2/name/"


def requisicao(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
    except:
        print('Erro na requisição em:', url)


def parsing(response_text):
    try:
        return json.loads(response_text)
    except:
        print('Erro ao fazer parsing.')


def qntd_de_paises(todos_paises):
    try:
        return len(todos_paises)
    except:
        print("Erro na contagem de países.")


def listar_paises(todos_paises):
    for pais in todos_paises:
        print(pais["name"])


def mostrar_populacao(nome_pais):
    res = requisicao(URL_NAME + nome_pais)
    if res:
        lista_paises = parsing(res)
        if lista_paises:
            for pais in lista_paises:
                print("Nome: {} , Total de habitantes: {}".format(pais["name"], pais["population"]))
        else:
            print("País não encontrado.")


def mostrar_moedas(nome_pais):
    res = requisicao(URL_NAME + nome_pais)
    if res:
        lista_paises = parsing(res)
        if lista_paises:
            for pais in lista_paises:
                print('Moedas do {}.'.format(pais['name']))
                moedas = pais["currencies"]
                for moeda in moedas:
                    print("  Código: {}\n  Name: {}\n  Simbolo: {}\r\n".format(moeda['code'], moeda['name'], moeda['symbol']))
        else:
            print("País não encontrado.")


if __name__ == "__main__":
    mostrar_moedas('por')