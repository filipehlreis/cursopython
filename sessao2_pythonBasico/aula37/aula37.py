"""
For in em Python
Iterando strings com for
Funcao range (start =0. stop, step=1)
"""
texto = 'python'

# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# for letra in texto:
#     print(letra)
#

#
# for n, letra in enumerate(texto):
#     print(n, letra)

#
# for n in range(20, 10, -2):
#     print(n)


nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
