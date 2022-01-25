# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> nao borda

# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall
# re.


import re

texto = """
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouviar a Maria:
"Jooooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
"""

# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\W+', texto))
# print(re.findall(r'\W+', texto, flags=re.A))
# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\S+', texto, flags=re.I))
# print(re.findall(r'\be\w+', texto, flags=re.I))
# print(re.findall(r'\w+e\b', texto, flags=re.I))
# print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
# print(re.findall(r'\w{4}', texto, flags=re.I))
# print(re.findall(r'flo\B', texto, flags=re.I))


texto2 = """
131.768.460-53sas
055.123.060-50 asdas
955.123.060-90
"""

# print(re.findall(r"\d{3}\.\d{3}\.\d{3}\-\d{2}", texto2))
# print(re.findall(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", texto2, flags=re.M))


texto3 = "O João gosta de folia E adora ser amado"
texto3 = "O João gosta de folia \n E adora ser amado"

# print(re.findall(r"^o.*o$", texto3, flags=re.I))
print(re.findall(r"^o.*o$", texto3, flags=re.I | re.S))
