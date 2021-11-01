from classes.conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)
        print('Conta poupanca criada com sucesso.')

    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= self._saldo:
                self._saldo -= valor
            else:
                print(f'O seu saldo é insuficiente para realizar a operação.')
        else:
            raise TypeError('O valor a ser sacado deve ser INT ou FLOAT')
