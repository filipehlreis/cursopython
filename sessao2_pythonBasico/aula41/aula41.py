"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteraveis
"""

string = 'O Brasil é o o o pais do futebol, o Brasil é penta.'

lista_1 = string.split(' ')

print(lista_1)
print(len(lista_1))

lista_2 = string.split(',')
print(lista_2)
print(len(lista_2))

lista_3 = string.split('ra')
print(lista_3)
print(len(lista_3))

for valor in lista_1:
    print(valor)

print()
print()

for valor in lista_1:
    print(f'a palavra "{valor}" apareceu {lista_1.count(valor)}x na frase.')

print('\n\n')

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

print('\n\n\n')

lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())

######################################################################
print('\n\n\n\n\n\n')

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = '_'.join(lista)

print(string)
print(lista)
print(string2)

#######################################################################

print('\n\n\n\n\n')

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista = [
    [0, 'Luiz'],
    [1, 'Joao'],
    [2, 'Maria'],
]

for indice, nome in lista:
    print(indice, nome)

print('\n\n')

lista = ['Luiz', 'Joao', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

n1, n2, n3 = lista
print(n2)
