# mutavel: listas, dicionarios mutaveis
# Imutavel: tuplas, strings, numeros,true, false, none


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista=[]
    lista.extend(clientes_iteravel)
    return lista

lista_de_clientes1 = ['fabricio']
clientes1 = lista_de_clientes(['Jao', 'maria', 'eduardo'], lista_de_clientes1)
clientes2 = lista_de_clientes(['marcos', 'jonas', 'zico'])
clientes3 = lista_de_clientes(['jose'])

print(clientes1)
print(clientes2)
print(clientes3)
