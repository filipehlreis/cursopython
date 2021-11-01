nome = 'Filipe'
idade = """28"""
altura = 1.75
e_maior = True
peso = 76.5
imc = 0.00
imc = peso / (altura * altura)


print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{0} tem {1} anos e seu IMC é {2:.2f}'.format(nome, idade, imc))