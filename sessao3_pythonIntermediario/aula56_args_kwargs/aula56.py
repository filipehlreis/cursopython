"""
Funcoes (def) em Python - *args **kwargs
"""


#
# def func(a1, a2, a3, a4, a5=None):
#     print(a1, a2, a3, a4, a5)
#     return a1, a2, a3
#
#
# var = func(1, 2, 3, 4)
# print(var)


def func(*args):
    args = list(args)
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


def fun(*args):
    for v in args:
        print(v)


def f(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('idade nao existe')

listaa = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
f(*listaa, *lista2, nome = 'Luiz', sobrenome = 'Miranda', idade=12 )
#
# lista = [1, 2, 3, 4, 5]
# print(*lista, sep='-')
#
# func(1, 2, 3, 4, 5)
