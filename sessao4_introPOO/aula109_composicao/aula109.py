from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()


cliente2 = Cliente('Maria', 55)
cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Joao', 19)
cliente3.inserir_endereco('Sao Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()


print('#'*50)

