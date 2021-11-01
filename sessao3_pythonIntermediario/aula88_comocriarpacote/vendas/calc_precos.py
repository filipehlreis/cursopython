from vendas.formata.preco import real


def aumento(valor, porcentagem, formata=False):
    r = valor * (1 + porcentagem / 100)
    if formata:
        return real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor * (1 - porcentagem / 100)

    if formata:
        return real(r)
    else:
        return r
