"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'x = {x}  y = {y}  z = {z}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(y = 1, x = 2, z = 3)