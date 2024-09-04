"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')
if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar: 
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Que horas são? ')
try:
    horas = int(horas)

    if horas >= 0 and horas <= 11:
        print('Bom dia')
    elif horas >= 12 and horas <= 17 :
        print('Boa tarde')
    elif horas >= 18 and horas <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome >= 7:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')