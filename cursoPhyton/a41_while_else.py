""" while / else"""

string = 'Qualquervalor'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
    print(letra)
    i += 1
else:  # Quando o laço é terminado, exacuta 
    print('Não encontrei espaço na string')
print('Fora do while')