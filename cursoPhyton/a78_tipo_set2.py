# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = tuple(s1)
print(l2)
print(3 in s1)


n1 = set('Gustavo')
print(n1)