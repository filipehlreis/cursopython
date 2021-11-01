"""
Zip - Unindo Iteraveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    cidades,
    estados,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)







