# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class A:
    atributo_a = 'valor_a'
    def metodo(self):
        print('A')

    def __init__(self, atributo):
        self.atributo = atributo

class B(A):
    atributo_b = 'valor_b'
    def metodo(self):
        print('B')

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

class C(B):
    atributo_c = 'valor_c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI, BURLEI O SISTEMA')

    def metodo(self):
        super().metodo() # B
        super(B, self).metodo() # A
        A.metodo(self)
        B.metodo(self)
        print('C')

# c = C()
c = C('Atributo', 'Qualquer')
print(C.mro()) # Method resolution order
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

print(c.atributo)
print(c.outra_coisa)