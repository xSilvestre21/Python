def encontrar_posicoes_cobra(matriz):
    posicoes = []
    
    # Encontrar a cabeça da cobra (representada pelo 'h')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 'h':
                cabeca = (i, j)
                break

    # Adicionar a cabeça primeiro na lista (invertendo a ordem das coordenadas)
    posicoes.append([cabeca[1], cabeca[0]])  # [coluna, linha]

    # Usar um set para registrar as posições já visitadas
    visitadas = set()
    visitadas.add(cabeca)

    # Função para verificar as posições vizinhas (sem usar direções)
    def vizinhos(i, j):
        vizinhos_pos = []
        # Verificar as células ao redor (cima, baixo, esquerda, direita)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Cima, Baixo, Esquerda, Direita
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matriz) and 0 <= nj < len(matriz[i]) and matriz[ni][nj] != ' ' and (ni, nj) not in visitadas:
                vizinhos_pos.append((ni, nj))
        return vizinhos_pos

    # Agora, vamos explorar os vizinhos a partir da cabeça
    while len(posicoes) < sum(1 for row in matriz for cell in row if cell != ' '):
        i, j = posicoes[-1]  # Pegar o último segmento adicionado
        for ni, nj in vizinhos(i, j):
            posicoes.append([nj, ni])  # Inverter a ordem antes de adicionar (coluna, linha)
            visitadas.add((ni, nj))
            break  # Adiciona o primeiro vizinho encontrado e segue para ele

    return posicoes

# Exemplo de uso
matriz = [
    " >>h   ",
    " ^   v ",
    " ^<<<< "
]

# Encontrar as posições da cobra
posicoes = encontrar_posicoes_cobra(matriz)

# Exibir as posições
print(posicoes)
