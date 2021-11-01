"""
Desafio validador de cpf

CPF = 168.995.350-09
-----------------------------------------
1 * 10 = 10             #     1 * 11 = 11 <-
6 *  9 = 54             #     6 * 10 = 60
8 *  8 = 64             #     8 *  9 = 72
9 *  7 = 63             #     9 *  8 = 72
9 *  6 = 54             #     9 *  7 = 63
5 *  5 = 25             #     5 *  6 = 30
3 *  4 = 12             #     3 *  5 = 15
5 *  3 = 15             #     5 *  4 = 20
0 *  2 =  0             #     0 *  3 =  0
                        # ->  0 *  2 =  0

        297             #              343
11 - (297 % 11) = 11    #  11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            # Digito 2 = 9
"""
#
# # cpf_original = '16899535009'
# cpf_original = '42005549843'
#
# novo_cpf = cpf_original[0:9]
# contador1 = 10
# soma_cpf1 = 0
# for numero in novo_cpf:
#     soma_cpf1 = soma_cpf1 + int(numero) * contador1
#     contador1 -= 1
#
# digito1 = 11 - (soma_cpf1 % 11)
# digito1 = 0 if digito1 > 9 else digito1
#
# print(soma_cpf1)
# print(digito1)
#
# print('\n#####\n')
# """
# #############
# """
#
# novo_cpf2 = novo_cpf + str(digito1)
# print(novo_cpf2)
#
# contador2 = 11
# soma_cpf2 = 0
#
# for numero in novo_cpf2:
#     # print(contador2)
#     soma_cpf2 = soma_cpf2 + int(numero) * contador2
#     contador2 -= 1
#
# # soma_cpf2 = soma_cpf2 + digito1 * contador2
#
# digito2 = 11 - (soma_cpf2 % 11)
# # digito2 = 0 if digito2 > 9 else digito2
#
# print(soma_cpf2)
# print(digito2)
#
# cpf_verificado = novo_cpf2 + str(digito2)
#
# if cpf_verificado == cpf_original:
#     print('CPF valido.')
# else:
#     print('CPF invalido.')
#
#
#
#
#


"""
SOLUCAO
VALIDADOR DE CPF
"""

# # cpf = '16899535009'
# cpf = '42005549843'
# novo_cpf = cpf[:-2]
# reverso = 10
# total = 0
#
# for index in range(19):
#     if index > 9:
#         index -= 9
#
#     total += int(novo_cpf[index]) * reverso
#
#     reverso -= 1
#     if reverso < 2:
#         reverso = 11
#         d = 11 - (total % 11)
#
#         if d > 9:
#             d = 0
#
#         total = 0
#         novo_cpf += str(d)
#
# print(novo_cpf)
#
# if novo_cpf == cpf:
#     print('CPF válido')
# else:
#     print('CPF inválido.')


"""
Gerando CPF Valido
"""



# cpf = '16899535009'
# cpf = '42005549843'
from random import randint
numero = str(randint(100000000,999999999))

novo_cpf = numero
reverso = 10
total = 0

for index in range(19):
    if index > 9:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)
#
# if novo_cpf == cpf:
#     print('CPF válido')
# else:
#     print('CPF inválido.')
#
