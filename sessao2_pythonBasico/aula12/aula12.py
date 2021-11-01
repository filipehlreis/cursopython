"""
Operadores Logicos
and, or, not
in e not in
"""

a = ''
b = 0
#
# if not a:
#     print('Preencha um valor para a')
# else:
#     print('a preenchido')
#
# nome = 'Filipe'
# if 'ili' in nome:
#     print('existe ')
# else:
#     print('nao existe')

usuario = input('Nome do usuario: ')
senha = input('Senha do ussuario: ')

usuario_bd = 'filipe'
senha_bd = '123456'

if (usuario in usuario_bd) and (senha == senha_bd):
    print('usuario logado')
else:
    print('usuario e/ou senha incorreta')
