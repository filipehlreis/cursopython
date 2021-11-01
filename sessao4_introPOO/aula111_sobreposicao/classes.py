class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print('Estou em CLIENTE')


class ClienteVIP(Cliente):
    # def falar(self):
    #     # super().falar()
    #     Pessoa.falar(self)
    #     Cliente.falar(self)
    #     print('Outra coisa qualquer')
    def __init__(self, nome, idade, sobrenome):
        # super().__init__(nome, idade)
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')
