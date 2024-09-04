# Manipulando chaves e valores em dicionários

pessoa = {}

...
...

chave = 'nome'

pessoa[chave] = 'Gustavo'
pessoa['sobrenome'] = 'Silvestre'
print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
