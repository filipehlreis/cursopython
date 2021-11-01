from classes.pessoa import Pessoa
from classes.cc import ContaCorrente
from classes.cp import ContaPoupanca


class Cliente(Pessoa):
    def __init__(self, nome, idade, agencia, numero, saldo, conta='cp', limite=1000):
        super().__init__(nome, idade)
        if conta == 'cp':
            self._conta = ContaPoupanca(agencia, numero, saldo)
        elif conta == 'cc':
            self._conta = ContaCorrente(agencia, numero, saldo, limite)
        else:
            print('Nao foi possivel criar a conta.')
