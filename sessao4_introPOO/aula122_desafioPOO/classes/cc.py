from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=1000):
        super().__init__(agencia, numero, saldo)
        self._limite = limite
        print('Conta Corrente criada com sucesso.')

    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= (self._saldo + self._limite):
                self._saldo -= valor
            else:
                print(f'O seu saldo é insuficiente para realizar a operação.')
        else:
            raise TypeError('O valor a ser sacado deve ser INT ou FLOAT')
