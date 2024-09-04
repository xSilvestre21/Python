# Desempacotamento em chamadas
# de métodos e funções
salas = [
#        0           1
    ['Mariana', 'Isabella', ],  # 0
#       0
    ['Luiza', ], # 1
#         0         1         2
    ['Giovanni', 'Mateus', 'Otávio', (0, 10, 20, 30, 40)], # 2
]

# a, b, *_, c = lista
# print(a, c)

# for nome in lista:
#     print(nome, end=' ')

# print('...............')
# print(*lista)
# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*string)
# print(*tupla)

print(*salas, sep = '\n')