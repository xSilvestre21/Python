"""
Cuidado com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
"""

# nome = 'Gustavo'
# outra_variavel = nome
# nome = 'Julia'
# print(nome)
# print(outra_variavel)

lista_a = ['Luiz', 'Maria', 1, True, 1.9]
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)