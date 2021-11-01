# lista = [0, 1, 2, 3, 4, 5]
# lista = iter(lista)
#
#
# print(hasattr(lista, '__iter__'))
#
# print(next(lista))
#
#
#
# # print(hasattr(lista,'__next__'))
#
# # for v in lista:
# #     print(v)
#


#
# import sys
#
# lista = list(range(100))
# # print(lista)
# print(sys.getsizeof(lista)/8/1024/1024)
import sys
import time

#
# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#         print(n)
#     return r
#
# g = gera()
#
# for v in g:
#     print(v)
#

#
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
#
# g = gera()
# #
# # for v in g:
# #     print(v)
#
#
#
# print(hasattr(g,'__iter  __'))
# print(hasattr(g,'__next__'))
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


#
# def gera():
#     variavel = 'Valor 1'
#     yield variavel
#     variavel = 'Valor 2'
#     yield variavel
#     variavel = 'Valor 3'
#     yield variavel
#     variavel = 'Valor 4'
#     yield variavel
#
#
# g=gera()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# g=gera()
# for v in g:
#     print(v)
#


lista = list(range(1000))
print(sys.getsizeof(lista))

print('\n\n')
lista2 = [x for x in range(100000)]
print(type(lista2))
print(sys.getsizeof(lista2))
lista2 = (x for x in range(100000 ))
print(type(lista2))
print(sys.getsizeof(lista2))

for v in lista2:
    print(v)



