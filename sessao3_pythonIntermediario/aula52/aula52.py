"""
Funcoes - def em Python (parte 1)
"""


def funcao():
    print('Hello world!')


funcao()
funcao()
funcao()


def saudacao(msg='OI', nome='Joao'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel1 = saudacao("Ola,", 'Filipe')
variavel2 = saudacao()


def funcao1(var):
    return var


variavel3 = funcao1('valor que eu quero')

if variavel3:
    print(variavel3)

else:
    print('nenhum valor')

"""
#########################################
"""


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(8.1, -4)

if divide:
    print(divide)
else:
    print("Conta invalida")

print('\n\n')


def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(var)
var('fybcai')
print('\n\n\n')


def dumb2():
    return ('Luiz', 'Otavio')


var2 = dumb2()
print(var2, type(var2))

var2[0] = 'jorge'
print(var2[0])
