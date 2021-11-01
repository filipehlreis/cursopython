from classes.cc import ContaCorrente
from classes.cp import ContaPoupanca
from classes.cliente import Cliente
from classes.banco import Banco

# c1 = ContaCorrente(111, 222, 0)
# c1.sacar(22)
# print(c1.saldo)
# c1.depositar(100)
# c1.detalhes()


cliente = Cliente('Luiz', 25, 1111, 2222, 0, 'cp')
cliente.sacar()