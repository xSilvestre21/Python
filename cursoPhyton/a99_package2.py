from sys import path

# https://stackoverflow.com/questions/2386714/why-is-import-bad


# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import soma_do_modulo, fala_oi
# from aula99_package.modulo import *

# print(__name__)
# print(*path, sep='\n')
# print(soma_do_modulo(2, 9))
# print(aula99_package.modulo.soma_do_modulo(2, 9))
# print(modulo.soma_do_modulo(2, 9))
# print(variavel)
# fala_oi()

import aula99_package

from aula99_package import soma_do_modulo, fala_Oi
print(aula99_package.soma_do_modulo(4, 5))
print(soma_do_modulo(4, 5))
fala_Oi()