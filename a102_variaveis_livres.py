# Variáveis livres + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        print(locals())
        return a
    return dentro


dentro = fora(10)
dentro2 = fora(20)

print(dentro())
print(dentro2())