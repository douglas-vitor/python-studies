import json
import sys

import requests

#Documentação API : https://restcountries.eu/
#Utilizado python 3
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


def qntd_de_paises():
    res = requisicao(URL)
    if res:
        lista_paises = parsing(res)
        if lista_paises:
            print("{} países no mundo.".format(len(lista_paises)))


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


def ler_arg2():
    try:
        arg2 = sys.argv[2]
        return arg2
    except:
        print("É preciso passar o nome de um país.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("##################################")
        print("# Bem vindo ao sistema de países #")
        print("##################################\r\n")
        print("  Uso: python paises.py <acao> <nome_do_país>\r\n")
        print("  Ações: contagem, moedas, populacao")

    else:
        arg1 = sys.argv[1]
        if arg1 == 'contagem':
            qntd_de_paises()
        
        elif arg1 == 'moedas':
            arg2 = ler_arg2()
            if arg2:
                mostrar_moedas(arg2)
        
        elif arg1 == 'populacao':
            arg2 = ler_arg2()
            if arg2:
                mostrar_populacao(arg2)

        else:
            print("Argumento inválido.")