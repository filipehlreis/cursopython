"""
count - Itertools
"""
#
# from types import GeneratorType
#
# variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
#
# print(isinstance(variavel, GeneratorType))


from itertools import count

contador = count()
lista = ['Luiz', 'Joao', 'Maria', 'Jose', 'Edu']

lista = zip(contador,lista)
print(list(lista))

#
# for valor in contador:
#     print(round(valor, 2))
#
#     if valor >= 10 or valor <= -10:
#         break
