from collections import deque
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    posicoes = []
    visitadas = set()
    
    # Encontrar a cabeça da cobra ('h')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'h':
                cabeca = (i, j)
                posicoes.append(cabeca)
                visitadas.add(cabeca)
                break
        else:
            continue
        break
    
    # Usar uma fila (deque) para explorar a cobra
    queue = deque([cabeca])
    
    # Direções possíveis: Cima, Baixo, Esquerda, Direita
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        i, j = queue.popleft()
        
        # Explorar os vizinhos
        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] != ' ' and (ni, nj) not in visitadas:
                posicoes.append((ni, nj))
                visitadas.add((ni, nj))
                queue.append((ni, nj))
    
    # Converter para formato [col, row]
    posicoes_invertidas = [[col, row] for row, col in posicoes]
    
    return posicoes_invertidas

grid = [
    " >>h   ",
    " ^   v ",
    " ^<<<< "
]

# Encontrar as posições da cobra
posicoes = find_snake_on_grid(grid)

# Exibir as posições
print(posicoes)
