class Multiplica:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            multiplicados = []
            for i in resultado:
                multiplicados.append(i * self._multiplicador)
            return multiplicados
        return interna
        

@Multiplica(10)
def tabuada(i):
    numeros = []
    for n in range(i, 100, i):
        numeros.append(n)
    return numeros

print(tabuada(6))




nome = 'Gustavo'
while True:
    encontrar = input('Digite a letra que desejaria encontrar: ')
    if encontrar in nome:
        print(f'{encontrar} está em {nome}')
        break
    else:
        print(f'{encontrar} não está em {nome}, tente novamente')



nome = 'Zlatan Ibrahimovic'
tamanho_nome = len(nome)
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print()
print(novo_nome)



frase = 'Olá, tudo bem? Me chamo Gustavo Silvestre e estudo engenharia da computação na unisal'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    print(letra_atual, qtd_apareceu_mais_vezes_atual)
    i += 1
    
     



