# https://docs.python.org/3/library/functions.html#open


"""
file = open('abc.txt', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')
file.write('Linha4\n')

file.seek(0, 0)
print('Lendo linhas: ')
print(file.read())
print('#' * 50)

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#' * 50)

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')
print('#' * 50)

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()
"""

"""
try:
    file = open('abc.txt', 'w+')
    file.write('linha')
    file.seek(0,0)
    print(file.read())
finally:
    file.close()
"""

"""
## modo mais pythonico de se fazer. pois a funcao with abre e ja fecha logo em seguida
with open('abc.txt', 'w+') as file:
    file.write('Linha 11\n')
    file.write('Linha 22\n')
    file.write('Linha 33\n')
    file.write('Linha 44\n')

    file.seek(0, 0)
    print(file.read())
print('#$' * 20)

with open('abc.txt', 'r') as file:
    print(file.read())

print('#$' * 20)
"""

"""
with open('abc.txt', 'a+') as file:
    file.write('outra linha\n')
    file.seek(0, 0)
    print(file.read())

import os

os.remove('abc.txt')
"""
import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}


d1_json = json.dumps(d1, indent=True)

with open('abc.txt', 'w+') as file:
    file.write(d1_json)
