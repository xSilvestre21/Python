"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Gustavo'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'
print(string)
print(outra_variavel)
print(string.upper())
print(string.zfill(100))
print(string.lower())
