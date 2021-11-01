from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)
    idade: int

    def __post_init__(self):
        # self.nome_completo = f'{self.nome} {self.sobrenome}'
        if not isinstance(self.nome, str):
            raise TypeError(f'Invalid type {type(self.nome)} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', '5', 2)
p2 = Pessoa('D', '3', 23)
p3 = Pessoa('F', '4', 54)
p4 = Pessoa('B', '6', 34)
p5 = Pessoa('E', '1', 23)

pessoas = [p1, p2, p3, p4, p5]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))

# print(p1 == p2)
# print(p1)
# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo)
print()

print(asdict(p1))
print(astuple(p1))
