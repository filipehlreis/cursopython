from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
# nova_lista2 = [x for x in lista if x > 5]
# print(list(nova_lista))
# print(list(nova_lista2))



#
# def filtra(produto):
#     if produto['preco'] > 50:
#         return True
#
# # novos_produtos = filter(lambda p: p['preco'] > 50, produtos)
# novos_produtos = filter(filtra, produtos)
#
# for produto in novos_produtos:
#     print(produto)


def filtra_idade(pessoa):
    if pessoa['idade'] <= 18:
        return True
    else:
        return False

nova_lista_pessoas = filter(filtra_idade, pessoas)
for pessoa in nova_lista_pessoas:
    print(pessoa)

