# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

dados = {'nome': 'Gustavo', 'idade': 20}
p1 = Pessoa(**dados)
# p1.nome = 'oi'
# print(p1.nome)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = ' EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)

print(vars(p1))
print(p1.nome)


        