# Try, except, else e finally

try:
    a = 18
    b = 0
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print('Dividiu por zero')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Número b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + Index Error')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESONHECIDO')
    

print('Continuar')