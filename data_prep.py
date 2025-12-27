import pandas as pd

def preparar_dados_looker():
    """
    Simula o tratamento de uma planilha do Google Sheets 
    antes de conectar ao Looker Studio.
    """
    # Dados de exemplo baseados no seu projeto
    dados = {
        'Data': ['2025-01-01', '2025-01-02', '2025-01-03'],
        'Vendas': [1200, 1500, 1100],
        'Meta': [1000, 1000, 1000]
    }
    
    df = pd.DataFrame(dados)
    
    # Calculando a performance da meta (Engenharia de Dados básica)
    df['Atingimento_%'] = (df['Vendas'] / df['Meta']) * 100
    
    print("Dados preparados para o Looker Studio:")
    print(df)

if __name__ == "__main__":
    preparar_dados_looker()
