# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro

def cria_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadriplicar = cria_multiplicador(4)
print(duplicar(25))
    



    
