"""
Considerando duas listas de inteiros ou floats (lista A e lista B).
Dome os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]


###############
resultado
lista_soma = [2,4,6,8]
"""
from itertools import zip_longest
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = list(zip(lista_a, lista_b))
# lista_soma = list(lista_soma)

# lista = [(a+b) for a, b in lista_soma]
lista = [(a + b) for a, b in zip(lista_a, lista_b)]
lista2 = [(a + b) for a, b in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista)
print(lista2)
