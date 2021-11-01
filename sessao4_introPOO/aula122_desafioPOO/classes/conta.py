from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia_conta):
        self._agencia = agencia_conta

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero_conta):
        self._numero = numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo_conta):
        self._saldo = saldo_conta

    def depositar(self, valor: float):
        if isinstance(valor, (int, float)):
            self._saldo += valor
            print(f'Status:\n\tO valor R$ {valor:.2f} foi depositado em sua conta.\n '
                  f'\tSeu saldo atual é R$ {self._saldo:.2f}.')
        else:
            raise TypeError('Esperado valor em INT ou FLOAT')

    @abstractmethod
    def sacar(self):
        pass

    def detalhes(self):
        info = f'Detalhes:\n' \
               f'\tAgência: {self._agencia}\n' \
               f'\tNumero da Conta: {self._numero}\n' \
               f'\tSaldo: R$ {self._saldo:.2f}'
        print(info)
