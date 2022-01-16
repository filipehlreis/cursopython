"""
Template Method (comportamental) tem a intencao de definir um algoritmo em um
metodo, postergando alguns passos para as subclasses por herança. Template
method permite que subclasses redefinam certos passos de um algoritmo sem
mudar a estrutura do mesmo.

Tambem é possivel defnir hooks para que as subclassses utilizem caso
necessario.

The Hollywood principle: "Don't Call Us, We'll Call You".
(IoC - Inversao de controle)
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Pizza(ABC):
    """Classe abstrata"""

    def prepare(self) -> None:
        """Template method"""
        self.hook_before_add_ingredients()  # Hook
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concreto
        self.serve()  # Concreto

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f"{self.__class__.__name__}: Cortando pizza.")

    def serve(self) -> None:
        print(f"{self.__class__.__name__}: Servindo pizza.")

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):

    def add_ingredients(self) -> None:
        print("AModa - adicionando ingredientes: pressunto, queijo, goiabada.")

    def cook(self) -> None:
        print('AModa - cozinhando por 45 min no forno a lenha.')


class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print("Veg - Lavando ingredients")

    def add_ingredients(self) -> None:
        print("Veg - adicionando ingredientes: brocolis, repolho, goiabada.")

    def cook(self) -> None:
        print('Veg - cozinhando por 5 min no forno comum.')


if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()
