# Meta caracteres:
# ^ -> comeca com
# $ -> termina com
# [^a-z] -> negacao


import re


cpf = 'a   147.852.963-12 qualquer coisa'
# cpf = '147.852.963-12'
# print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^a-z]+', cpf))
print(re.findall(r'[^0-9]+', cpf))
print(re.findall(r'[^ a-z]+', cpf))
