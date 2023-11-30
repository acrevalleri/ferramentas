import json
import sys

import requests

URL = 'https://restcountries.com/v2/all'

URL_PAIS = 'https://restcountries.com/v2/name'

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('erro ao fazer requisição: {}'.format(url))


def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('erro ao fazer o parsing')


def contagem():
    resposta = requisicao(URL)
    if resposta:
        lista_de_pais = parsing(resposta)
        if lista_de_pais:
            return len(lista_de_pais)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])


def listar_populacao(nome_pais):
    resposta = requisicao('{}/{}'.format(URL_PAIS, nome_pais))
    if resposta:
        lista_pais = parsing(resposta)
        if lista_pais:
            for pais in lista_pais:
                print('{}: {}'.format(pais['name'], pais['population']))
        else:
            print('pais nao encontrado')



def mostrar_moedas(nome_pais):
    resposta = requisicao('{}/{}'.format(URL_PAIS, nome_pais))
    if resposta:
        lista_pais = parsing(resposta)
        if lista_pais:
            for pais in lista_pais:
                print('moeda do', pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
        else:
            print('pais nao encontrado')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('## bem vindo à api de paises ##')
        print('usage: python api_paises.py <opcao> <pais>')
        print('opcoes: contagem, moeda, populacao')
    else:
        arg1 = sys.argv[1]

        if arg1 == "contagem":
            nmr_paises = contagem()
            print('Existem {} paises no mundo'.format(nmr_paises))
        elif arg1 == "moeda":
            try:
                pais = sys.argv[2]
                mostrar_moedas(pais)
            except:
                print('É preciso passar o nome do pais')
        elif arg1 == "populacao":
            try:
                pais = sys.argv[2]
                listar_populacao(pais)
            except:
                print('É preciso passar o nome do pais')
        else:
            print('argumento invalido')

