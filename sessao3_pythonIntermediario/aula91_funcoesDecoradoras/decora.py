# # def fala_oi():
# #     print('oi')
# #
# # fala_oi()
# #
# #
# # variavel = fala_oi
# #
# # print(type(variavel))
#
#
#
#
#
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('agora estou decorada')
#         funcao(*args, **kwargs)
#
#     return slave
#
# @master
# def fala_oi():
#     print('oi')
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
# # variavel = master( fala_oi)
# # variavel()
# # fala_oi = master(fala_oi)
# # fala_oi()
#
# outra_funcao('ola, eu sou filipe')
# outra_funcao()
#


from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA funcao {funcao.__name__} levou'
              f' {tempo:.2f}ms para executar')
        return resultado

    return interna


@velocidade
def demora():
    for i in range(300000):
        print(i, end='')
        # sleep(1)


demora()
