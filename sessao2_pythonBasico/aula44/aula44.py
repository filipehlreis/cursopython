"""
trocar valores de variaveis sem criar outras variaveis
"""

x = 10
y = 'Luiz'
z = 'otavio'

x, y, z = z, x, y

print(f'x= {x} e y={y} e z={z}')
