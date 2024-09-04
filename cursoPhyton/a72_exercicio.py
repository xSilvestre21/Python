# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

def multiplica(*args):
    produto = 1
    for numero in args:
        produto = produto * numero
    return produto
   
total = multiplica(1, 2, 3, 27)
print(total)

# Crie uma função que fala se um número é par ou impar.
# Retorne se o número é par ou ímpar

def par_ou_impar(num):
    condicao = num % 2 == 0
    variavel = f'[{num}] Seu número é par' if condicao else f'[{num}] Seu número é ímpar'
    return variavel

print(par_ou_impar(77))
print(par_ou_impar(100))
print(par_ou_impar(36))


            