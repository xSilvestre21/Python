#isinstance - para saber se o objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), 
    {0, 1}, {'nome': 'Gustavo'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print('Set')
        print(item, isinstance(item, set))
        print('')

    elif isinstance(item, str):
        print('Str')
        print(item.upper())
        print('')

    elif isinstance(item, (int, float)):
        print('Num')
        print(item, item * 2)
        print('')

    else:
        print('Outro')
        print(item)
        print('')