from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import soma_do_modulo, fala_oi
from aula99_package.modulo import *

print(__name__)
# print(*path, sep='\n')
print(soma_do_modulo(2, 9))
print(aula99_package.modulo.soma_do_modulo(2, 9))
print(modulo.soma_do_modulo(2, 9))
print(variavel)
fala_oi()