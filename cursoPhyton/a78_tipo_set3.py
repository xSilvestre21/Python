# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Gustavo')
s1.add(21)
s1.update(('Hello world', 1, 2, 3, 4))

#s1.clear()
s1.discard('Hello world')
print(s1)