def divide(x, y):
    return x / y


def cria_func(func, y):
    def interna(x):
        return func(x, y)
    return interna

divide_por_dois = cria_func(divide, 2)
print(divide_por_dois(10))