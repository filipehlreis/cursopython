"""
* Criar variaveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves_)
"""


nome = "Filipe"
idade = 28
altura = 1.75
peso = 76.5
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / (altura * altura)

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso:.2f}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')









