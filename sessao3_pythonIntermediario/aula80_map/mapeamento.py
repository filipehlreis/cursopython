from dados import produtos, pessoas, lista


# nova_lista = map(lambda x: x * 2, lista)
# nova_lista2 = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))
# print(nova_lista2)

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.2)
    return p


novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

nomes = map(lambda p: p['nome'], pessoas)
nova_idade = map(aumenta_idade,pessoas)

for idade in nova_idade:
    print(idade)