from classes import *

"""
Associacao - Usa | Agrecacao - Tem | Composicao - É dono | Herança - É
"""

c1 = Cliente('Luiz', 45)
print(c1.nome)

a1 = Aluno('Maria', 54)
print(a1.nome)

c1.falar()

c1.comprar()
a1.estudar()

p1 = Pessoa('Joao', 32)
p1.falar()
