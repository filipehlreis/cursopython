"""
Composite é um padrao de projeto estrutural que permite que voce utilize
a composicao para criar objeos em estruturas de arvores. O padrao permite aos
clientes tratarem de maneira uniforme objetos individuais (Leaf) e composicoes
de objetos (composite)

IMPORTANTE: so aplique este padrao em uma estrutura que possa ser representada
em formato hierarquico (arvore).

No padrao composite, temos dois tipos de objetos:
Composite - que representa nós internos da arvore
Leaf - que  representa nós externos da arvore.

Objetos Composite sao objetos mais complexos e com filhos. Geralmente, eles
delegam trabalho para os filhos usando um metodo em comum.
Objetos Leaf sao objetos simples, da pont e sem filhos. Geralmente, sao esses
objetos que realizam o trabalho real da aplicacao.

"""
