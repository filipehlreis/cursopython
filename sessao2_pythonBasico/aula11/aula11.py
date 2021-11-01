"""
Operadores relacionais

== > >= < <= !=

"""
#
# print(2 == 1)
#
# print(50 == '2')

# print('\n\n\n\n')

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar emprestimo
idade_limite_inferior = 20  # muito jovem
idade_limite_superior = 30  # muito velho
if (idade >= idade_limite_inferior) and (not(idade <= idade_limite_superior)):
    print(f'Emprestimo permitido para {nome}.')
else:
    print(f'Emprestimo negado para {nome}.')