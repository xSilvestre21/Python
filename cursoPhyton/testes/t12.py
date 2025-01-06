def escolhe_taxi(tf1,vqr1,tf2,vqr2, d):
    tax_1_dez_menos = float(tf1) + float(vqr1) * d
    tax_2_dez_menos = float(tf2) + float(vqr2) * d
    tax_1_dez = float(tf1) + float(vqr1) * d
    tax_2_dez = float(tf2) + float(vqr2) * d
    tax_1_dez_mais = float(tf1) + float(vqr1) * d
    tax_2_dez_mais = float(tf2) + float(vqr2) * d

    print(d)
    
    if tax_1_dez_menos > tax_2_dez_menos:
        if tax_1_dez > tax_2_dez:
            if tax_1_dez_mais > tax_2_dez_mais:
                return 'Empresa 2'
              
    if tax_2_dez_menos > tax_1_dez_menos:
        if tax_2_dez > tax_1_dez:
            if tax_2_dez_mais > tax_1_dez_mais:
                return 'Empresa 1'
              
    if tax_1_dez_menos == tax_2_dez_menos:
        if tax_1_dez == tax_2_dez:
            if tax_1_dez_mais == tax_2_dez_mais:
                return 'Tanto faz'
              
    if tax_1_dez_menos > tax_2_dez_menos:
        mensagem = 'Empresa 2 quando a distância < 10.0, '
    elif tax_2_dez_menos > tax_1_dez_menos:
        mensagem = 'Empresa 1 quando a distância < 10.0, '
    else:
        mensagem = 'Tanto faz quando a distância < 10.0, '

    if tax_1_dez > tax_2_dez:
        mensagem2 = 'Empresa 2 quando a distância = 10.0, '
    elif tax_2_dez > tax_1_dez:
        mensagem2 = 'Empresa 1 quando a distância = 10.0, '
    else:
        mensagem2 = 'Tanto faz quando a distância = 10.0, '

    if tax_1_dez_mais > tax_2_dez_mais:
        mensagem3 = 'Empresa 2 quando a distância > 10.0'
    elif tax_2_dez_mais > tax_1_dez_mais:
        mensagem3 = 'Empresa 1 quando a distância > 10.0'
    else:
        mensagem3 = 'Tanto faz quando a distância > 10.0'
        
    return f'{mensagem}{mensagem2}{mensagem3}'

print(escolhe_taxi('1', '2.5', '3', '2', 7.14))