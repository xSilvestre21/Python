# Yield from

def gen1():
    print('Começou gen 1')
    yield 1
    yield 2
    yield 3
    print('Acabou gen 1')

def gen2(gen= None):
    print('Começou gen 2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Acabou gen 2')

def gen3():
    print('Começou gen 3')
    yield 10
    yield 20
    yield 30
    print('Acabou gen 3')


g = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for num in g:
    print(num)
print()
for num in g2:
    print(num)
print()
for num in g3:
    print(num)