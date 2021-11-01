"""
1 - Crie uma funcao que exibe uma saudacao com os parametros saudacao e nome.
"""


def saudacao(msg, nome):
    print(f'{msg} {nome}')


saudacao('Ola,', 'Filipe')

"""
2 - Crie uma funcao que recebe 3 numeros como parametros e exiba a soma entre eles
"""


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(2, 3, 4)

"""
3 - Crie uma funcao que receba 2 numeros. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro numero somado do
aumento do percentual do mesmo.
"""


def percentual(valor, percentual):
    return valor * (1 + (percentual / 100))


percent = percentual(120, -10)
print(percent)

"""
4 - Fizz Buzz - se o parametro da funcao for divisivel por 3, retorne fizz,
se o parametro da funcao for divisivel por 5, retorne buzz. se o parametro da 
funcao for divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o
numero enviado
"""


def fizzBuzz(numero):
    if not numero % 5:
        if not numero % 3:
            return 'FizzBuzz'
        else:
            return 'Buzz'
    elif not numero % 3:
        return 'Fizz'
    return numero


print(fizzBuzz(1), 1)
print(fizzBuzz(2), 2)
print(fizzBuzz(5), 5)
print(fizzBuzz(9), 9)
print(fizzBuzz(15), 15)
print(fizzBuzz(25), 25)
print(fizzBuzz(50), 50)
print(fizzBuzz(62), 62)
print(fizzBuzz(65), 65)
print(fizzBuzz(75), 75)
print(fizzBuzz(100), 100)
