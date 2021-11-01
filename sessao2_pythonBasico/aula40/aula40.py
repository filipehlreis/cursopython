"""
For / Else em Python
"""

variavel = ['Luiz Otavio', 'Joaozinho', 'Maria']
#
# comeca_com_j = False
# for valor in variavel:
#     # if valor.startswith('L'):
#     #     print('Comeca com L', valor)
#     # else:
#     #     print('nao comecao com L', valor)
#     if valor.lower().startswith('j'):
#         comeca_com_j = True
# if comeca_com_j:
#     print('Existe uma palavra com J')
# else:
#     print('nao existe uma palavra com j')

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('nao existe uma palavra que comeca com J')
