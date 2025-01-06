# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

pessoas = ['Gustavo', 'Guilherme', 'André', 'Mateus']


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter((product(*camisetas)))