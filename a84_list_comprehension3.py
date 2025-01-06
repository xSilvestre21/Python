# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 > 10)
]

# print(*novos_produtos, sep='\n')
# print(10 * '-')
p(novos_produtos)
print(10 * '-')


lista = [n for n in range(10) if n < 5]
print(lista)