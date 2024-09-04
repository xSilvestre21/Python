primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    input(f'Primeiro valor[{primeiro_valor}] é maior que o segundo[{segundo_valor}].')
elif segundo_valor > primeiro_valor:
    input(f'Segundo valor[{segundo_valor}] é maior que o primeiro[{primeiro_valor}].')
else:
    print('Os valores são iguais.')
