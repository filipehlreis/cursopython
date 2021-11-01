# """
# https://rszalski.github.io/magicmethods/
# """
#
#
# class A:
#
#     def __new__(cls, *args, **kwargs):
#         print('eu sou o new')
#         cls.nome = 'Luiz Otavio'
#
#         def haha(*args, **kwargs):
#             print('Fala OI')
#
#         cls.haha = haha
#
#         return super().__new__(cls)
#
#     def __init__(self):
#         print('Eu sou o INIT')
#
#
# a = A()
# print(a.nome)
# a.haha()


class A:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste

    def __init__(self):
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado

    def fala_oi(self):
        print('Oi')

    def __setattr__(self, key, value):
        print(key, value)
        if key == 'nome':
            self.__dict__[key] = 'Voce nao pode fazer isso.'
        else:
            self.__dict__[key] = value

    def __del__(self):
        print('Objeto coletado.')

    def __str__(self):
        return 'Essa é a class A criada para tal coisa'

    def __len__(self):
        return 55

a = A()
# b = A()
# c = A()
#
# print(id(a), id(b), id(c))
#
# variavel = a(1, 2, 3, 4, 5)
# print(variavel)
# a.fala_oi()
# print()
# a.nome = 'Luiz otaavio'
# print(a.nome)
print(a)
print(len(a))

print('#' * 50)
