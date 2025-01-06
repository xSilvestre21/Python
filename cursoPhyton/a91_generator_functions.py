# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1 # Pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais uma...')
    yield 3 # Pausar
    print('Vou terminar')
    return 'ACABOU'

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

for n in gen:
    print(n)


def gerador(n = 0, maximum = 10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return
        

gen_2 = gerador(n = 5, maximum=15)
# for n in gen_2:
#     print(n)

print(gen_2.__next__())
print(gen_2.__next__())
print(gen_2.__next__())
