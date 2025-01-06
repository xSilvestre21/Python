def encontrar_posicoes_cobra(matriz):
    posicoes = []
    cabeca = ()
    # Passo 1: Encontrar a cabeça da cobra ('h')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 'h':
                cabeca = (i, j)
                break
        else:
            continue
        break

    # Adicionar a cabeça na lista
    posicoes.append(cabeca)

    # Passo 2: Usar um set para registrar as posições já visitadas
    visitadas = set()
    visitadas.add(cabeca)

    # Passo 3: Função para explorar os vizinhos (cima, baixo, esquerda, direita)
    def explorar_vizinhos(i, j):
        vizinhos_pos = []
        # Cima (-1, 0), Baixo (1, 0), Esquerda (0, -1), Direita (0, 1)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matriz) and 0 <= nj < len(matriz[i]) and matriz[ni][nj] != ' ' and (ni, nj) not in visitadas:
                vizinhos_pos.append((ni, nj))
        return vizinhos_pos

    # Passo 4: Explorar a cobra
    while len(posicoes) < sum(1 for row in matriz for cell in row if cell != ' '):
        i, j = posicoes[-1]  # Pega o último segmento da cobra
        vizinhos = explorar_vizinhos(i, j)  # Busca os vizinhos conectados
        for ni, nj in vizinhos:
            # Adiciona o próximo segmento encontrado na lista
            posicoes.append((ni, nj))  # Mantém o formato [linha, coluna]
            visitadas.add((ni, nj))
            break  # Adiciona o primeiro vizinho encontrado e continua

    # Passo 5: Inverter os índices na lista de resultados
    posicoes_invertidas = [[col, row] for row, col in posicoes]

    return posicoes_invertidas

# Exemplo de uso
matriz = [
    " >>>h   ",
    " ^   v ",
    " ^<<<< "
]

# Encontrar as posições da cobra
posicoes = encontrar_posicoes_cobra(matriz)

# Exibir as posições
print(posicoes)
