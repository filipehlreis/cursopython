carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 2', 50))

# total = [(x, y) for x, y in carrinho]
total = sum([float(y) for x, y in carrinho])  # solucao do professor
"""
nao curti a solucao do professor por cauas que durante a proposta do professor, ele
deixou a entender que era pra fazer a soma dentro do list comprehension, e nao deixou
a entender que poderia usar sum(lista).
"""
print(carrinho)
print(total)

#
# soma = 0
# [soma := soma + y for x, y in carrinho]
#
#
#
# print(soma)
#
# print('\n')
#
# soma = 0
#
# for x, y in carrinho:
#     soma += y
#
# print(soma)
#
# #########################################
#
# # total = 0
# # for produto in carrinho:
# #     total += produto[1]
# #
# #
# # print(carrinho)
# # print(total)
#
# # total = []
# # for produto in carrinho:
# #     total.append(produto[1])
# # print(carrinho)
# # print(total)
#
# ######################
