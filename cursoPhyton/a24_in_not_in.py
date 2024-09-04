# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# G u s t a v o
#-7-6-5-4-3-2-1

nome = 'Gustavo'
print(nome[3])
print(nome[-3])
print(10 * '.')
print('a' in nome)
print('z' in nome)
print(10 * '.')

encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')