# Métodos de classes + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônima', idade)
        

p1 = Pessoa('Gustavo', 20)
p2 = Pessoa.criar_com_50_anos('Fernando')
p3 = Pessoa.criar_anonimo(23)
p4 = Pessoa('Anônima', 25)

print(Pessoa.ano)
Pessoa.metodo_de_classe()
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)