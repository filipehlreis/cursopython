def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um numero: '))

    if numero is None:
        print('Isso nao é numero')
    else:
        print(numero + 21)
        print(numero * 5)
