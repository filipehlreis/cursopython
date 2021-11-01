"""
EM PYTHON TUDO È UM OBJETO: incluindo classes
Metaclasses sao as "classes" que criam classes.
type é uma metaclasse (!!!???)
"""

"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, voce precisar criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, nao atributo em {name}')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'valor'
    # b_fala='wow'
    def sei_la(self):
        pass

    def b_fala(self):
        print('OI')

"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


class C(B):
    attr_classe = 'Valor C'


class Pai:
    nome = 'teste'

D = type(
    'A',
    (Pai,),
    {
        'attr': 'Ola mundo!'
    }
)

c = C()
print(c.attr_classe)

d = D()
print(d.attr)
print(d.nome)