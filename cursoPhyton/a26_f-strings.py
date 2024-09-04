"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou x - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou _
EX.: 0>100, .1f
Conversion flags - !r !s !a
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:.^10}')
print(f'{1000.3543545324343:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')