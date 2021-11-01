"""
Formatando valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(NUMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro


"""

num_1 = 1
# num_2 = 3
# divisao = num_1 / num_2
# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')
# nome = 'filipe'
# print(f'{nome:.2s}')

print(num_1)
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 151
print(f'{num_3:0^10}')

print(f'{num_3:0>10.2f}')
nome = 'Filipe Henrique leite dos reis'
tamanho = 40-len(nome)
print(f'{nome:#^{tamanho}}')

nome_formatado = '{:@>10}'.format(nome)
nome_formatado = '{:*<20}'.format(nome_formatado)

print(f'{nome_formatado:.20s}')
print(f'{nome.ljust(20, "$" ) }')
print()
print()
print()
print(nome.lower())
print(nome.upper())
print(nome.title())
print(nome)


