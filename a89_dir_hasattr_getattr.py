# dir, hasattr e getattr em Python
string = 'Gustavo'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string.upper())
else:
    print('Não existe o método', metodo)