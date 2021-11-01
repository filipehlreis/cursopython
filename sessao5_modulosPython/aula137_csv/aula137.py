import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)
    # next(dados)
    # dados = csv.DictReader (arquivo)
    dados = [x for x in csv.DictReader(arquivo)]

    # for dado in dados:
    #     print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

# print(dados)


# for dado in dados:
#     print(dado)


with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL

    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
            [
                chaves[0],
                chaves[1],
                chaves[2],
                chaves[3],
            ]
        )


    for dado in dados:
        # print(dado['Nome'])
        escreve.writerow(
            [
                # dado['Nome'],
                # dado['Sobrenome'],
                # dado['E-mail'],
                # dado['Telefone']
                dado[chaves[0]],
                dado[chaves[1]],
                dado[chaves[2]],
                dado[chaves[3]]
            ]
        )
