#
# d1 = {'chave1':'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave'
#
# print(d1)
# print(d1['chave1'])
#


# d1 = {'chave' : 'valor', 'chave' : 'valor'}
# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# d1['nova_chave'] = 'Valor da nova chave'
#
# print(d1)
#
#############
# d1 = {1: 'valor', 2: 'valor2', 3: 'valor da real da chave'}
# print(d1)
# print()
# print(d1[2])


################
# d1 = {
#     'str': 'valor',
#     123: 'Outro valor',
#     (1, 2, 3, 4): 'tupla'
# }


#################################################
# d1['naoexiste'] = 'agora existe'
# if 'naoexiste' in d1:
#     print(d1['naoexiste'])
#
# d1['nomedachave'] = 'teste do nome da chave'
# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))
#
# d1.update({'nova_chave': 'novo_valor'})
#
# print(d1.get('nova_chave'))
#
# print('\n\n')
# print(d1)
# # del d1['str']
# print(d1)
#
# print('\n\n')
#
# print('str' in d1)
# print('valor' in d1.values())
###########################################
# d1 = {
#     'chave1': 'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'tupla'
# }
#
# print(len(d1))
#
# for k in d1:
#     print(k)
# print()
# print()
# for v in d1.values():
#     print(v)
#
# print()
#
# for k in d1.items():
#     print(k[0], k[1])
#
# print()
# print()
# for k, v in d1.items():
#     print(k, v)
#
#
###########################################

#
# clientes = {
#     'cliente1': {
#         'nome': 'Luiz',
#         'sobrenome': 'Otavio',
#     },
#     'cliente2': {
#         'nome': 'Filipe',
#         'sobrenome': 'Henrique',
#     },
#     'cliente3': {
#         'nome': 'Maria',
#         'sobrenome': 'Reis',
#     },
#     'cliente4': {
#         'nome': 'Jorge',
#         'sobrenome': 'Leite',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')
#


###########################################


d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otavio']}
v = d1.copy()

print(d1)
print(v)

v[1] = 'Luiz'

print(d1)
print(v)
v['d'][1] = 'Joaozinho'

print()
print(d1)
print(v)


