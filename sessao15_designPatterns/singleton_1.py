"""
O Singleton tem a intencao de garantir que uma classe tenha somente uma
instancia e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found that we still love them all.
(Not really - I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
-Erich Gamma, em entrevista para informIT
https://
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()

    print(as1.tema)
    # as3 = AppSettings()

    # print(as1)
    # print(as2)

    # as1.nome = 'Luiz'
    # print(as3.nome)
