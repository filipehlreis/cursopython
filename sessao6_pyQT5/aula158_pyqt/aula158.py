"""
SOLUCAO
VALIDADOR DE CPF
"""
import re


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)
    if not cpf or len(cpf) < 11:
        return False
    novo_cpf = cpf[:-2]
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

    # print(novo_cpf)

    if novo_cpf == cpf:
        return True
    else:
        return False


"""
Gerando CPF Valido
"""

from random import randint


def gera_cpf():
    numero = str(randint(100000000, 999999999))

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

    return novo_cpf
