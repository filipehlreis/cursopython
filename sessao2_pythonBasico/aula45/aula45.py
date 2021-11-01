"""
operador ternario em python
"""

logged_user = False
#
# if logged_user:
#     msg = 'Usuario Logado.'
# else:
#     msg = 'Usuario precisa logar.'

#
# msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'
#
# print(msg)
#
# idade = 18
#
# if idade >= 18:
#     print('Pode acessar.')
# else:
#     print('nao pode acessar.')
#
# msg = 'Pode acessar.' if idade >= 18 else 'Nao pode acessar.'
# print(msg)

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    msg = 'Voce precisa digitar apenas numeros.'
else:
    eh_de_maior = int(idade) >= 18
    msg = 'Pode acessar.' if eh_de_maior else 'Nao pode acessar.'

print(msg)
