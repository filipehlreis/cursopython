"""
Monostate (ou Borg) - è uma variacao do Singleton proposto por Alex Martelli
que tem a intencao de garantir que o estado do objeto seja igual para todas
as instancias.
"""


from typing import Dict


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k} = {v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoState(StringReprMixin):
    _state: Dict = {
        'x': 10,
        'y': 20,
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None):
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class A(MonoState):
    pass


if __name__ == "__main__":
    m1 = MonoState(nome='Luiz')
    m2 = A(sobrenome='Miranda')
    # m1.x = 'Qualquer coisa'
    print(m1)
    print(m2)
