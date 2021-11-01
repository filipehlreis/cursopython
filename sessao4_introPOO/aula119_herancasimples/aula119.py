"""
Animal -> respirar (é um animal)
    Lobo(Animal) -> respirar / uivar (Lobo é um Lobo e um Animal)
        Cachorro(Lobo) -> respirar / uivar / latir
        (Cachorro, é um Cachorro, tambem é um Lobo() e um Animal ())

"""

"""
Biblioteca
    Interface(Biblioteca)
        metodo_da_interface
"""

from classes.interface import Interface

i1 = Interface()
i1.metodo_da_interface()
i1.chama_metodo_da_interface()