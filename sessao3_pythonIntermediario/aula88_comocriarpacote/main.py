# import vendas.calc_precos
# from vendas import calc_precos

from vendas.calc_precos import aumento, reducao
# from vendas.formata.preco import real

preco_original = 49.90
# preco_com_aumento = calc_precos.aumento(preco, 15)
# preco_com_aumento = vendas.calc_precos.aumento(preco, 15)
preco_com_aumento = aumento(valor=preco_original, porcentagem=15, formata=True)
preco_com_reducao = reducao(valor=preco_original, porcentagem=15, formata=True)
print(preco_com_aumento)
print(preco_com_reducao)
