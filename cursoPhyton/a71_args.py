"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)
print('.............')
def soma(*args):
    # print(args)
    # print(args, type(args))
    total = 0
    for numero in args:
        total = total + numero
    return total

soma1_2_3 = soma(1, 2, 3)
print(soma1_2_3)
print('.............')
soma4_5_6 = soma(4, 5, 6)
print(soma4_5_6)
print('.............')
outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 78, 10)
print(outra_soma)
print('.............')
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)

print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))
print('.............')

print(numeros, *numeros)