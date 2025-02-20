# Atributos de classes
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade  # Se no lugar do nome da classe utilizar o self vai puxar o outro valor. 
    

p1 = Pessoa('Gustavo', 20)
p2 = Pessoa('Marcos', 32)

# Pessoa.ano_atual = 1

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
        