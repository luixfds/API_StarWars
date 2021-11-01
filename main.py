#   importando a biblioteca requests e a json para pegar a api e convertela
import requests
import json


#   iniciando as variaveis de imput e preparando a requisição dinamica
tipo = input("people? planets? ou starships?: ") + "/"
id = input(f"id: ") + "/"
request = str(tipo) + str(id)


#   tente executar:
try:
    #   atribui o link base da api na variavel
    swapi = requests.get("https://swapi.dev/api/" + request)
    #   converte para json
    swapi = swapi.json()

    #   exibe todos os dados da api base mais os atribuidos pelo input
    print("\ntodos os dados: " + str(swapi) + "\n")

 #   caso nao consiga, faça:
except:
    print('valor invalido!')


#   tente executar:
try:
    #   se o input tiver sido "people" traga os valores abaixo:
    if tipo == "people/":
        swapi_aux = swapi['name'], \
                    swapi['species'], \
                    swapi['birth_year'], \
                    swapi['homeworld']

        #   exiba os valores escolhidos do tipo people
        print("nome, especie, aniversario e planeta natal: " + str(swapi_aux))

    #   se o input tiver sido "planets" traga os valores abaixo:
    elif tipo == "planets/":
        swapi_aux = swapi['name'], \
                    swapi['terrain'], \
                    swapi['population']

        #   exiba os valores escolhidos do tipo planets
        print("nome, bioma e população: " + str(swapi_aux))

    #   se o input tiver sido "starships" traga os valores abaixo:
    elif tipo == "starships/":
        swapi_aux = swapi['name'], \
                    swapi['model'], \
                    swapi['passengers'], \
                    swapi['cargo_capacity'], \
                    swapi['hyperdrive_rating']

        #   exiba os valores escolhidos do tipo starships
        print("nome, modelo, passageiros, capacidade de carga e Hyperdrive Rate: " + str(swapi_aux))

#   caso nao consiga, faça:
except:
    print("Não foi encontrado dados com este id, lamento...")

