import os

caminho_arquivo = 'aula116.txt'

# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Atenção\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo) mesma coisa que o unlink

# os.rename(caminho_arquivo, 'aula116-2.txt')