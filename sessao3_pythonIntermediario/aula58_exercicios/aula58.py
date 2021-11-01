"""
1 - Crie uma funcao 1 que recebe uma funcao2 como parametros e retorne o valor da
funcao2 executada.
"""
#
# def funcao1(funcao2):
#     return funcao2()
#
# def funcao2():
#     return 2+4
#
# variavel = funcao1(funcao2)
# print(variavel)

#
# def ola_mundo():
#     return 'Ola mundo!'
#
# def mestre(funcao):
#     return funcao()
#
# execurantando = mestre(ola_mundo)
# print(execurantando)


"""
2 - Crie uma fncao 1 que recebe uma funcao2 como parametro e retorne o valor 
da funcao executada. Faca a funcao1 executar duas funcoes que recebam um numero
diferente de argumentos
"""


#
# def funcao1(**kwargs):
#     nome = kwargs.get('nome')
#     saudacao = kwargs.get('saudacao')
#
#     if nome != None:
#         funcao_oi(nome)
#     if nome != None and saudacao != None:
#         funcao_saudacao(nome, saudacao)
#
#
# def funcao_oi(nome):
#     print(f'Oi {nome}')
#
#
# def funcao_saudacao(nome, saudacao):
#     print(f'{saudacao} {nome}')
#
#
# funcao1(nome='FFilipe',saudacao='Ola mundo,')

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Filipe')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia')
print(executando)
print(executando2)
