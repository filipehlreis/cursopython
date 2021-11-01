"""
Combinations, Permutations e Product - Itertools
Combinacao - Ordem nao importa
Permutacao - Ordem importa
ambos nao repetem valores unicos
Produto - ordem importa e repetevalores unicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Amdre', 'Eduardo', 'leticia', 'fabricio', 'rose']

# c = 0
# for grupo in combinations(pessoas, 2):
#     c += 1
#     print(c)
#     print(grupo)

# c = 0
# for grupo in permutations(pessoas, 2):
#     c += 1
#     print(c)
#     print(grupo)

c = 0
for grupo in product(pessoas, repeat=3):
    c += 1
    print(c)
    print(grupo)
