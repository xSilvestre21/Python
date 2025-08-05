# Funções decoradoras e decoradores com classes

class Time:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        class_name = self

class Planeta:
    def __init__(self, nome):
        self.nome = nome


barcelona = Time('Barcelona')
corinthians = Time('Corinthians')

terra = Planeta('Terra')
marte = Planeta('Marte')

