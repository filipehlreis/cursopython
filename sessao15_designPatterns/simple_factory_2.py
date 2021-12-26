"""
Na programacao POO, o termo factory (fabrica) refere-se a uma classe ou metodo 
que é responsavel por criar objetos.

Vantagens:
    Permitem criar um sitema com baixo acoplamento entre classes porque ocultam
    as classes que criam os objetos do codigo cliente.

    Facilitam a adicao de novas classes ao codigo, porque o cliente nao conhece
    e nem utiliza a implementacao da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criacao de "singletons" porque a 
    fabrica pode retornar um objeto já criado para o cliente, ao inves de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no codigo.

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory.

Nessa aula:
    Simple Factory <- Uma especie de Factory Method parametrizado
    Simple Factory pode nao ser considerado um padrao de projeto por si so
    Simple Factory pode quebrar principios do SOLID
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente ...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente ...")


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular está buscando o cliente ...")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto de luxo está buscando o cliente ...")


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo nao existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto', 'moto_luxo']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
