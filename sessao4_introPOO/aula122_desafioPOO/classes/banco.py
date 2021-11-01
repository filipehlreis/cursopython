class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []

    def listar_clientes(self):
        for k, cliente in enumerate(self._clientes):
            print(f'Cliente {k + 1}:\n'
                  f'\t{cliente}')

    def listar_contas(self):
        for k, conta in enumerate(self._contas):
            print(f'Conta {k + 1}:\n'
                  f'\t{conta}')

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)
        print(f'Cliente "{cliente.nome}" foi inserido com sucesso.')

    def inserir_conta(self, conta):
        self._contas.append(conta)
        print(f'Conta foi inserido com sucesso.')

    def checar_agencia(self, agencia):
        if agencia in self._contas:
            return True
        else:
            return False

    def checar_cliente(self, cliente):
        if cliente in self._clientes:
            return True
        else:
            return False

    def checar_conta(self, conta):
        if conta in self._contas:
            return True
        else:
            return False
