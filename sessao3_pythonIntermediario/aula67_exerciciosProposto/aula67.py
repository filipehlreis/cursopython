string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
# print(len(string))

# lista = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
# retorno_final = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
#
# comp = [letra for letra in string]
# print(comp)

# print(string[0:10])
# print(string[0:10])

k = 0
# print(f'{string[k % 10:k % 10 + 10]}')

# minha solucao apos ver o inicio do professor
comp = [string[k % 10:k % 10 + 10] for k, v in enumerate(string) if k % 10 == 0]
print(comp)

# solucao do professor
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
print(lista)

retorno = '.'.join(lista)
print(retorno)