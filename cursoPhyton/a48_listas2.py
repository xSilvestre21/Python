"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, Ler, Alterar, Apagar = lista [i] (CRUD)
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])

lista.append(70)
lista.pop()
lista.append(80)
lista.append(90)
ultimo_valor = lista.pop(3)
print(lista, 'Removido: ', ultimo_valor)