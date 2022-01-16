"""
Template Method (comportamental) tem a intencao de definir um algoritmo em um
metodo, postergando alguns passos para as subclasses por herança. Template
method permite que subclasses redefinam certos passos de um algoritmo sem
mudar a estrutura do mesmo.

Tambem é possivel defnir hooks para que as subclassses utilizem caso
necessario.

The Hollywood principle: "Don't Call Us, We'll Call You".
(IoC - Inversao de controle)
"""

from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): pass

    def base_class_method(self):
        print("Ola eu sou da classe abstrata e serei executado tambem  ")

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print("olha, eu vou utilizar o hook.")

    def operation1(self):
        print('Operacao 1 concluida')

    def operation2(self):
        print('Operacao 2 concluida')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operacao 1 concluida (de maneira diferente)')

    def operation2(self):
        print('Operacao 2 concluida (de maneira diferente)')


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
