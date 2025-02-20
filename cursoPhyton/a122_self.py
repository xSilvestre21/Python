# Métodos em instâncias em Python
# Hard coded - É algo que foi escrito diretamente no código
# Insância de class (objeto) - Tem dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(blablabla, nome):
        blablabla.nome = nome

    def acelerar(abc):
        print(f'{abc.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)
 
celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
