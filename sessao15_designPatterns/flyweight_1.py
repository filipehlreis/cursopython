"""
Flyweight é um padrao de projeto estrutural que tem a intencao de usar
compartilhamento para suportar eficientemente grandes quantidades de objetos
de forma granular.

Só use o Flyweight quando TODAS as condicoes a seguir forem verdadeiras:
    - uma aplicacao utiliza uma grande quantidade de objetos;
    - os custos de armazenamento sao altos por causa da grande quantidade
    de objetos;
    - a maioria dos estados de objetos podem se tornar extrinsecos;
    - muitos objetos podem ser substituidos por poucos objetos compartilhados;
    - a aplicacao nao depende da identidade dos objetos.

Importante:
    - Estado intrinseco é o estado do objeto que nao muda, esse estado deve
    estar dentro do objeto flyweight;
    - Estado extrinseco é o estado do objeto que muda, esse estado pode ser
    movido para fora do objeto flyweight;


Dicionario:
Intrinseco - que faz parte de ou que constitui a essencia, a natureza de algo;
que é próprio de algo; inerente.
Extrinseco - que nao pertence a essencia de algo; que é exterior.
"""

from __future__ import annotations
from typing import Dict, List


class Client:
    """ Context """

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_address(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """ Flyweight """

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighbourhood, address_details,
            self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado.')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto.')

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='000000-000'
    )
    a2 = address_factory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'Casa'
    luiz.add_address(a1)
    luiz.list_address()

    joana = Client('Luiz')
    joana.address_number = '250'
    joana.address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_address()

    print(a1 == a2)
