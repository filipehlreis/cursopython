"""
Pilhas e filas
Pilha (stack) - LIFO - Last In, First Out
                Exemplo: Pilha de livros que sao adicionados um sobre o outro.
Fila (queue)  - FIFO - First In, First Out
                Exemplo: Uma fila de banco (ou qualquer fila da vida real)
                Filas podem ter efeitos colaterais em desempenho, porque a cada item
                alterado todos os indices serao modificados.
"""
#
# livros = list()
# livros.append('Livro 1')
# livros.append('Livro 2')
# livros.append('Livro 3')
# livros.append('Livro 4')
# livros.append('Livro 5')
#
# livro_removido = livros.pop()
# livro_removido = livros.pop()
# livro_removido = livros.pop()
# livro_removido = livros.pop()
# livro_removido = livros.pop()
#
# print(livros, livro_removido)


"""
 0  1   2   3   4   5   6   7   8   9
[1  2   3   4   5   6   7   8   9   10]


"""

from collections import deque

# fila = deque(maxlen=5)
# fila.append('joaozinho')
# fila.append('maria')
# fila.append('otavio')
# fila.append('marcos')
# fila.append('jose')
# print(f'Saiu:\t{fila.popleft()}')
# print(f'Saiu:\t{fila.popleft()}')
# print(f'Saiu:\t{fila.popleft()}')
# print(f'Saiu:\t{fila.popleft()}')
# print(f'Saiu:\t{fila.popleft()}')
# print(f'Saiu:\t{fila.popleft()}')
#
# print()
# for nome in fila:
#     print(nome)
#

# fila.extend([1, 2, 3, 4])
# fila.append(5)
# fila.append(6)
# fila.append(7)

# print(fila)


from time import sleep

fila = deque(maxlen=10)

# for i in range(1000):
#     fila.append(i)
#     sleep(1)
#     print(fila)


# fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fila.extend([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# fila.insert(2, 'luiz otabio')
# fila.extendleft([1, 2])
print(fila.index(30, 0, 5))
