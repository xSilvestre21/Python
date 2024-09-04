"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <Outro valor>
"""

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)