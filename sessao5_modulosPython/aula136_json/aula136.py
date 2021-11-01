"""

"""

from dados import *
import json

# lista = [1, 2, 3, 4, 5, 6]
# dados_json = json.dumps(lista)
#
# print(type(dados_json), dados_json)
#
# dados_json2 = json.dumps(clientes_dicionario, indent=4)
# print(type(dados_json2), dados_json2)
#
# ######################
# # print(clientes_json)
#
# dicionario = json.loads(clientes_json2)
# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)


with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)