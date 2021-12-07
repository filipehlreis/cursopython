from calculadora import soma

print(soma(10, 20))
print(soma(-10, 20))
print(soma(1.5, 2.5))
print(soma(15, 15))


try:
    print(soma(2, 's'))
except AssertionError as e:
    print(f'conta invalida: {e}')
    print(f'conta invalida: {e}')


