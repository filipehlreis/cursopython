"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1   x   x
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2   = 65 ##
Formula -> 11 - (65 % 11) = 1
Primeiro Digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   x
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2   = 67 ##
Formula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo Digito = 0

Novo CNPJ + Digitos =   04.252.011/0001-10
CNPJ Original       =   04.252.011/0001-10
Valido

Recap.
543298765432    -> Primeiro Digito
6543298765432   -> Segundo Digito
"""

import cnpj

if __name__ == '__main__':
    # cnpj_original = "04.252.011/0001-10"
    # cnpj_original = "40.688.134/0001-61"
    # cnpj_original = "71.506.168/0001-11"
    # cnpj_original = "12.544.992/0001-05"
    # cnpj_original = "89.788.295/0001-16"
    # cnpj_original = "13.792.366/0001-92"
    # cnpj_original = "99.682.809/0001-08"
    # cnpj_original = "91.098.147/0001-11"
    cnpj_original = "71.493.031/0001-70"

    cnpj_validando, cnpj_original_format = cnpj.valida_cnpj(cnpj_original)

    if not cnpj_validando:
        print(f'O CNPJ "{cnpj_original}" não é valido.')
    else:
        cnpj_validando = cnpj.calcula_digitos(cnpj_validando)
        cnpj.cnpj_validado(cnpj_original, cnpj_original_format, cnpj_validando)
