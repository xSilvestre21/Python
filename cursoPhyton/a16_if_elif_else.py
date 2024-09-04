# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(21)
elif entrada == 'sair':
    print('Você saiu no sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('Fora dos blocos')