# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Lucas', cliente1)
cliente1.append('Sérgio')

cliente2 = adiciona_clientes('Gabriel')
adiciona_clientes('Marcos', cliente2)


cliente3 = adiciona_clientes('Maria')
adiciona_clientes('Clara', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)