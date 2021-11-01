from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('Joao', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente nao autenticado.')

print('#' * 50)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(00)
    cliente2.conta.sacar(20)
else:
    print('Cliente nao autenticado.')

print('#' * 50)

if banco.autenticar(cliente3):
    cliente3.conta.depositar(40)
    cliente3.conta.sacar(20)
else:
    print('Cliente nao autenticado.')
