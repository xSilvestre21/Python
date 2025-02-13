# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(a, b, /, x, y): # Tudo que vem antes da barra não deve receber nome na chamada da função
    print(a + b, x + y)

soma(1, 2, 3, y=3)

def soma2(a, b, *, c): # Só funciona se o C for nomeado
    print(a + b + c)

soma2(1, 2, c=3)
