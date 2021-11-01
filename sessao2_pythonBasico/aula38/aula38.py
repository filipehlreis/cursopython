"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#
# texto = 'Valor'
#
# # indices 0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']
# #        -5   -4   -3   -2   -1
#
# string = 'ABCDE'
#
# print(lista)
# print()
# lista[4] = 'qualquer coisa'
# print(lista)
# print()
# print(lista[:3])
# print()
# print(lista[3:])
# print()
# print(lista[1:5:2])
# print()
# print(lista[::2])
# print()
# # print(string[1])

#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
#
# print(l2)
# l2.insert(0, 'banana')
# print(l2)
# l2.pop()
# print(l2)

#     0  1  2  3  4  5  6  7  8


# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(l2)
# l2.insert(2, 'banana')
# print(l2)
# del (l2[2])
# print(l2)
#
# print(max(l2))
# print(min(l2))
#
# # l1 = list(range(1,10))
# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l1)
#
# print()
#
# soma = 0
# for valor in l1:
#     soma = soma + valor
#     print(soma)
#
# l2 = ['String', True, 10, -20.5]
#
# for elem in l2:
#     print(f'O tipo de {elem} é {type(elem)}')


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Aaaaah isso nao vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)
    print(digitadas)

    if letra in secreto:
        print(f'Uhuuuul, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'Afffffz: a letra "{letra}" NAO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCE GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances')
    print()
