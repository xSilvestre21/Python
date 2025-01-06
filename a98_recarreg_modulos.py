import importlib

import a98_modulo

print(a98_modulo.variavel)

for i in range(10):
    importlib.reload(a98_modulo)
    print(i)

print('Fim')
