try:
    a = {}

    try:
        a = 1 / 0
    except:
        print('erro')
except NameError as erro:
    print('erro: ', erro)
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave')
except Exception as erro:
    print('ocorreu um erro inesperado.', erro)
else:
    print('seu codigo foi executado com sucesso!')
    print(a)
finally:
    print('finalmente.')  # utilizado para fechar algum arquivo
    # ou banco de daods que foi aberto anteriormente
    a = 0

print(a)
print('bora continuar')
