# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Gustavo', 'Silvestre')
# p1.nome = 'Gustavo'
# p1.sobrenome = 'Silvestre'

p2 = Pessoa('Tilia', 'Fonseca')
# p2.nome = 'Tilia'
# p2.sobrenome = 'Fonseca'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)