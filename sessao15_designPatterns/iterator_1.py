"""
Iterator é um padrao comportamental que tem a intencao de forneer um meio de
acessar, sequencialmente, os elementos de um objeto agregado sem expor sua
representacao subjacente.

    - Uma olecao deve fornecer um memio de acessar seus elementos sem expor
    suas estrutura interna.
    - Uma colecao pode ter maneiras e percursos diferentes para expor seus
    elementos.
    - Vode deve separar a complexidade dos algoritmos de iteracao da colecao
    em si.

A ideia principal do padaro é retirar a responsabilidade de acesso e percurso
de uma colecao, delegando tais tarefass para um objeto iterador.
"""

from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        # pra deixar igual no python
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        # return MyIterator(self._items)
        return self._my_iterator  # pra deixar igual no python

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"


if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Luiz')
    mylist.add('Maria')
    mylist.add('Joao')

    # print(mylist)

    # print('Roubei um valor: ', next(mylist.__iter__()))
    # print('Roubei um valor: ', mylist.__iter__().next())

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
