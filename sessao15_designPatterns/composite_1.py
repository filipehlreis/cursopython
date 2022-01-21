"""
Composite é um padrao de projeto estrutural que permite que voce utilize
a composicao para criar objeos em estruturas de arvores. O padrao permite aos
clientes tratarem de maneira uniforme objetos individuais (Leaf) e composicoes
de objetos (composite)

IMPORTANTE: so aplique este padrao em uma estrutura que possa ser representada
em formato hierarquico (arvore).

No padrao composite, temos dois tipos de objetos:
Composite - que representa nós internos da arvore
Leaf - que  representa nós externos da arvore.

Objetos Composite sao objetos mais complexos e com filhos. Geralmente, eles
delegam trabalho para os filhos usando um metodo em comum.
Objetos Leaf sao objetos simples, da pont e sem filhos. Geralmente, sao esses
objetos que realizam o trabalho real da aplicacao.

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure (ABC):
    """ Component """

    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """ Composite """

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":

    # Leaf
    camiseta1 = Product('camiseta1', 49.90)
    camiseta2 = Product('camiseta2', 19.90)
    camiseta3 = Product('camiseta3', 10.90)

    # Composite
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    # caixa_camisetas.print_content()

    # Leaf
    smartphone1 = Product('smartphone1', 9000)
    smartphone2 = Product('smartphone2', 11000)

    # Composite
    caixa_smartphone = Box('Caixa de Smartphone')
    caixa_smartphone.add(smartphone1)
    caixa_smartphone.add(smartphone2)

    # caixa_smartphone.print_content()

    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphone)
    caixa_grande.print_content()
    print(caixa_grande.get_price())
