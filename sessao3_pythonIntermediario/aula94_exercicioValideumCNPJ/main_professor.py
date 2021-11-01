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

import cnpj_professor

cnpj1 = '04.252.011/0001-10'
cnpj1 = '04.-1aaaaaaaaaaaaaaaaaaaaaaaaaaaa0'
# cnpj1 = '11.111.111/1111-11'

if cnpj_professor.valida(cnpj1):
    print(f'O CNPJ "{cnpj1}" é válido.')
else:
    print(f'O CNPJ "{cnpj1}" é inválido.')


for i in range(100):
    novo_cnpj = cnpj_professor.gera()
    formatado = cnpj_professor.formata(novo_cnpj)
    print(formatado)