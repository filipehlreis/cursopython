"""
Manipulando Strings - ala 6
*strings indices
*fatiamento de strings [inicio:fim:passo]
*funcoes built-in len, abs,type, print, etc...
essas funcoes podem ser usadas diretamente em cada tipo
"""


texto = "Python_s2"

print( texto[0] )
print( texto[-9] )

nova_string = texto[:6]
print(nova_string)

nova_string = texto[7:]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[:-1]
print(nova_string)

nova_string = texto[0::2]
print(nova_string)

tamanho = len(texto)
nova_string = texto[0:tamanho:3]
print(nova_string)






