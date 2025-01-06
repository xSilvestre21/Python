lista_de_numeros = [n for n in range(0, 100, 8)]
print(lista_de_numeros)



caixa = set()
for n in range(0, 10):
    caixa.add(n)
print(caixa)



pessoa = {
    'Nome': 'Gustavo',
    'Sobrenome': 'Silvestre',
    'Idade': 19,
    'Numero': 21
}
d1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in pessoa.items()
}
print(d1)

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')




lista = [
    {'nome': 'Gustavo', 'sobrenome': 'Silvestre'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

l1 = sorted(lista, key=lambda item: item['nome'])
print(l1)