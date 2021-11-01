import random
import string

# Gera um numero inteiro entre A e B
# inteiro = random.randint(10, 20)

# Gera um numero aleatorio usando a funcao range()
inteiro = random.randrange(900, 1000, 10)

# Gera um numero de ponto flutuante entre A e B
# flutuante = random.uniform(10,20)

# Gera um numero de ponto flutuante entre 0 e 1
flutuante = random.random()

#

lista = ['luiz', 'otabio', 'maria', 'rose', 'jenny', 'danilo', 'felipe']

# Seleciona aleatoriamente valores de uma lista
# sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2)
sorteio = random.sample(lista, 2)

# embaralha a lista
random.shuffle(lista)

# gera senha aleatoria
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres

senha = random.choices(geral, k=20)

for i in range(1000):
    senha = "".join(random.choices(geral, k=20))
    print(senha)
