# Decoradores com parâmetros
def fabrica_de_funcoes(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res + 20
    return aninhada

def blablabla(a, b, c):
    print(a, b, c)
    return fabrica_de_funcoes

@blablabla(1, 2, 3)   # Eu mesmo executo


def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)