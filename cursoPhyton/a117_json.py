import json

# pessoa = {
#     'nome' : 'Gustavo',
#     'sobrenome' : 'Silvestre',
#     'enderecos' : [
#         {'rua': 'R1', 'numero' : 264},
#         {'rua': 'R2', 'numero' : 442},
#     ],
#     'altura': 1.9,
#     'numeros_preferidos' : (21, 11, 10, 8, 7),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w') as arquivo:
#     json.dump(pessoa, 
#               arquivo, 
#               ensure_ascii=False,
#               indent=2
#     )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])