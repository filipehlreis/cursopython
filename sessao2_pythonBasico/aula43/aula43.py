"""
Desempacotamento de listas e Python
"""

lista = ['Luiz', 'Joao', 'Maria', 1, 2, 3, 4, 5, 6, 7, 9, 100]
n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1)
print(n2)
print(outra_lista)
print(ultimo_da_lista)

print('\n##############\n')

*outra_lista, n1, n2, n3 = lista

print(n1)
print(n2)
print(n3)
print(outra_lista)