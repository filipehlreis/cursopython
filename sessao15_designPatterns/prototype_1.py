"""
Especificar os tipos de objetos a serem criados usando uma instancia-prototipo
e criar novos objetos pela copia desse prototipo.
---
Quais objetos sao copiados com o sinal de atribuicao?

Mutaveis (passados por referencia)
    list
    set
    dict
    class (o usuario pode mudar isso)
    ...

Imutaveis (copiados)
    bool
    int
    float
    tuple
    str
    ...
"""

from __future__ import annotations
from copy import deepcopy
from typing import List


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":

    print('\n')
    luiz = Person('Luiz', 'Miranda')
    endereco_luiz = Address('Av Brasil', '250A')
    luiz.add_address(endereco_luiz)

    # esposa_luiz = deepcopy(luiz)
    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Leticia'

    print(luiz)
    print(esposa_luiz)
