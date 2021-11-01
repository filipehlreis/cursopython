def valida_cnpj(cnpj_original):
    cnpj_validando = remove_caract(cnpj_original)
    cnpj_original_format = convert_int_cnpj(cnpj_validando)
    cnpj_validando = convert_int_cnpj(cnpj_validando)
    cnpj_validando = conta_caract_cnpj(cnpj_validando)
    return cnpj_validando, cnpj_original_format


def remove_caract(cnpj_validando):
    cnpj_validando = cnpj_validando.replace("/", "")
    cnpj_validando = cnpj_validando.replace(".", "")
    cnpj_validando = cnpj_validando.replace("-", "")
    return cnpj_validando


def conta_caract_cnpj(cnpj_validando):
    if len(cnpj_validando) == 14:
        return cnpj_validando[0:-2]
    else:
        return False


def calcula_digitos(cnpj_validando):
    primeiro_digito = cnpj_primeiro_digito(cnpj_validando)
    cnpj_validando.append(primeiro_digito)
    segundo_digito = cnpj_segundo_digito(cnpj_validando)
    cnpj_validando.append(segundo_digito)
    return cnpj_validando


def convert_int_cnpj(cnpj_validando):
    cnpj_validando = [int(x) for x in cnpj_validando]
    return cnpj_validando


def cnpj_validado(cnpj_original, cnpj_original_format, cnpj_validando):
    if cnpj_original_format == cnpj_validando:
        print(f'O CNPJ "{cnpj_original}" é válido.')
    else:
        print(f'O CNPJ "{cnpj_original}" não é válido.')


def cnpj_primeiro_digito(cnpj_validando):
    cnpj_validador_digito1 = [x if x < 10 else x - 8 for x in range(13, 1, -1)]
    soma_digito1 = sum([(cnpj_validando[x] * cnpj_validador_digito1[x]) for x in range(0, 12, 1)])
    primeiro_digito = 11 - (soma_digito1 % 11)
    if primeiro_digito > 9:
        primeiro_digito = 0
    return primeiro_digito


def cnpj_segundo_digito(cnpj_validando):
    cnpj_validador_digito2 = [x if x < 10 else x - 8 for x in range(14, 1, -1)]
    soma_digito2 = sum([(cnpj_validando[x] * cnpj_validador_digito2[x]) for x in range(0, 13, 1)])
    segundo_digito = 11 - (soma_digito2 % 11)
    if segundo_digito > 9:
        segundo_digito = 0
    return segundo_digito


if __name__ == '__main__':
    pass
