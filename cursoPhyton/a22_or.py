# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras.
# Se qualquer tipo de valor for considerado falso,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

senha = input('Senha: ') or 'Sem senha'
print(senha)