"""
Higher Oder Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Salveeee', 'Luiz')
print(v)

"""
Higher Order Functions - Funções que podem receber 
e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como
outros tipos de dados comuns 
(strings, inteiros, etc...)
"""