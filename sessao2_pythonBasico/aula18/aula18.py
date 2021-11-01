"""
While em Python - aula 7
utilizado para realizar acoes enquanto uma condicao for verdadeira.

Requisitos: entender condicoes e operadores
"""
import os

#
# while True:
#     nome = input("Qual o seu nome? ")
#     print(f'Olá {nome}!')

x = 0
#
# while x < 10:
#     x = x + 1
#
#     if x == 3:
#         continue
#     print(x)
#
#     if x == 5:
#         break
#
#
# y = 0
# while x < 3:
#     y = 0
#     while y < 3:
#         print(f'({x},{y})')
#         y += 1
#
#     x += 1
#
# print('Acabou')


while True:
    print()
    sair = input('deseja sair?')
    if sair == 's' or sair == 'S':
        break

    num_1 = input('Digite um numero: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro numero: ')

    if not (num_2.isdigit() and num_1.isdigit()):
        continue
    else:
        num_1 = int(num_1)
        num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '%':
        print(num_1 % num_2)
    elif operador == '**':
        print(num_1 ** num_2)

print('acabou')
