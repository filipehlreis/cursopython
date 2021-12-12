from typing import Any, Callable, Dict, Iterable, List, NewType, Sequence, Union, Tuple

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Luiz Otavio'

# Sequencias
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'luiz')

# Dicionarios e conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]
pessoa: Dict[str, Union[str, int]] = {
    'nome': 'luiz otavio', 'sobrenome': 'Miranda', 'idade': 30}
pessoa2: MeuDict = {
    'nome': 'luiz otavio', 'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(82930840932)


def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao


def retorna_funcao2(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def fala_oi():
    print('oi')


def soma(x: int, y: int) -> int:
    return x + y


retorna_funcao(fala_oi)()

print(retorna_funcao2(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]


print(iterar([1, 2, 3]))
# deeve-se fazer Union caso envie outra coisa alem de int
print(iterar((1, 2, 3)))


print(iterar2([1, 2, 3]))
# deeve-se fazer Union caso envie outra coisa alem de int
print(iterar2((1, 2, 3)))
