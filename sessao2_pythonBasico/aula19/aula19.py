"""
While/ else - aula 8

contadores
acumuladores

"""

contador = 1
acumulador = 0

while contador <= 10:
    print(contador, acumulador)

    if contador == 3:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')
print('isso sera executado')
