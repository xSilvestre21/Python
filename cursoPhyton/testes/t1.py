
from datetime import datetime

def valida_data(data_str):
    """ Valida se a data está no formato DD/MM/AAAA e se é uma data válida. """
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        return None

def main():
    # Dados dos medicamentos e suas datas de vencimento
    medicamentos = {
        "Medicamento A": datetime(2025, 3, 25),
        "Medicamento B": datetime(2025, 1, 1),
        "Medicamento C": datetime(2024, 12, 29),
        "Medicamento D": datetime(2025, 10, 15),
        "Medicamento E": datetime(2024, 10, 15)
    }

    # Leitura da data de referência
    data_referencia_str = input().strip()
    
    # Validação da data de referência
    data_referencia = valida_data(data_referencia_str)
    
    if data_referencia is None:
        print("ERRO")
        return
    
    # Encontrar os medicamentos vencidos
    vencidos = [(nome, vencimento) for nome, vencimento in medicamentos.items() if vencimento <= data_referencia]
    
    # Exibir o resultado
    if vencidos:
        # Ordena os medicamentos vencidos pela data de vencimento
        vencidos.sort(key=lambda x: x[1])
        # Apenas os nomes dos medicamentos, separados por vírgula e espaço
        resultado = ", ".join(nome for nome, _ in vencidos)
        print(resultado)
    else:
        print("NENHUM")

if __name__ == "__main__":
    main()
