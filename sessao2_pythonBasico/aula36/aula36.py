# Indices
# 0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
nova_string = ''

print(tamanho_frase)

contador = 0

input_do_usuario = input('Qual letra deseja colocar maiuscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += frase[contador]
    contador += 1

print()
print(nova_string)
