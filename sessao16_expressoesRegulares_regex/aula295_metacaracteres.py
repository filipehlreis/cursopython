# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com excecao de quebra de linha)
# [] conjunto de caracteres

import re

texto = """
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouviar a Maria:
"Jooooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
"""

print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'.oão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[Jj]oão|[Mmabcdef]aria', texto))
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
print(re.findall(r'[Jj]oãO|[Mm]ariA', texto))
print(re.findall(r'jOãO|mAriA', texto, flags=re.I))
