from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joaozino')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()