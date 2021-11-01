"""
Modulos padrao do Python:
Modulos sao arquivos .py (que contem codigo python) e servem para expandir
as funcionalidades padrao da linguagem.
Vejatodos os modulos padrao do python em:
https://doc.python.org/3/py-modindex.html
"""

# import sys
from sys import platform as sistemaoperacional

# print(sys.platform)
print(sistemaoperacional)

# import random
from random import randint

# for i in range (10):
#     print(random.randint(0,10))

for i in range(10):
    print(randint(0, 10))

"""
# from random import *     ## isto significa que está importando tudo do modulo random, 
porem, vai ser mais dificil de saber de onde vem a funcao, qual a origem da funcao, e
pode ser que acabe sobreescrevendo alguma funcao do modulo.
"""
