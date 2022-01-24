# Meta caracteres: ^ $
# [@#a-zA-Z0-9]
# (abc|def)
# () \1
# () () \1 \2
# (())() \1 \2 \3


import re
from pprint import pprint

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
"""

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>', texto))


# tags = (re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)', texto))
# tags = (re.findall(r'(<([pdiv]{1,3})>(?:.*?)<\/\2>)', texto))

# tags = (re.findall(r'(<([pdiv]{1,3})>(?:.*?)<\/\2>)', texto))

# tags = (re.findall(r'<(?P<tag>[pdiv]{1,3})>(.*?)<\/(?P=tag)>', texto))

print()

# pprint(tags)
# for tag in tags:
#     um, dois, tres = tag
#     print(tres)


print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS "\3" COISAS \4', texto))


# cpf = '147.852.963-12'
# print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
# print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))
# print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
