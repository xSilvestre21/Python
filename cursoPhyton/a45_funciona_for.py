"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

"""

texto = iter('Luiz')   #__iter__()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

print(25 * '.')

# for lettra in texto
texto2 = 'Luiz'
iterador = iter(texto2) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

print('..............................')


for letra in texto: #Não vai fazer
    print(letra)
