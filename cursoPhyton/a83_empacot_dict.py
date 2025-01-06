# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Gustavo',
    'sobrenome': 'Silvestre',
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(10 * '-')
print(b1, b2)
print(10 * '-')

for chave, valor in pessoa.items():
    print(valor)
print(10 * '-')

# args e kwargs
# args (já vimos)
# kwargs - keyword (arguments nomeados)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, 'chave': 1, **dados_pessoa}

print(pessoa_completa)
print(10 * '-')

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome = 'Gustavo', numero = 21)
print(10 * '-')
mostro_argumentos_nomeados(**pessoa_completa)
print(10 * '-')

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)






