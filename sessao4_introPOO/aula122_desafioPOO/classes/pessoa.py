class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self._idade = idade
        else:
            raise TypeError("Idade precisa ser um valor inteiro.")


