def possibilities(word):
    letras = {
        '.': ['E'],
        '-': ['T'],
        '..': ['I'],
        '.-': ['A'],
        '...': ['S'],
        '..-': ['U'],
        '.-.': ['R'],
        '.--': ['W'],
        '-.': ['N'],
        '--': ['M'],
        '-..': ['D'],
        '-.-': ['K'],
        '--.': ['G'],
        '---': ['O']
    }

    ordem = ["E", "T", "I", "A", "S", "U", "R", "W", "N", "M", "D", "K", "G", "O"]

    def gerador_de_possibilidades(word):
        if '?' not in word:
            return [word]
        
        possibilidades = []
        for troca in ['.', '-']:
            possibilidades.extend(gerador_de_possibilidades(word.replace('?', troca, 1)))
        return possibilidades
    
    letras_possiveis = gerador_de_possibilidades(word)

    resultado = []
    for letra in letras_possiveis:
        if letra in letras:
            resultado.extend(letras[letra])
   
    return sorted(set(resultado), key=lambda x: ordem.index(x))