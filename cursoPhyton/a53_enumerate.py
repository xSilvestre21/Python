lista = ['Maria', 'Giovanni', 'André']
lista.append('Joao')

# lista_enumerada = enumerate(lista)

for indice, nome in enumerate(lista, start=21):
    print(indice, nome)


lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
