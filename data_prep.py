import pandas as pd

def clean_marketing_data():
    """
    Simula o saneamento de dados de marketing para evitar 
    duplicidade de categorias e erros de geolocalização.
    """
    # Dados brutos simulando seus prints (Artigos e Campanhas)
    raw_data = {
        'Artigo': ['Escuta ativa ', 'escuta ativa', 'Gestão de Projetos'],
        'Categoria': ['ux', 'UX', 'Gestão'],
        'Data': ['2021-06-01', '2021-06-02', '2021-06-03']
    }

    df = pd.DataFrame(raw_data)

    print("--- Iniciando Limpeza para Looker Studio ---")

    # 1. Padronização de strings (Evita que 'UX' e 'ux' sejam lidos como categorias diferentes)
    df['Categoria'] = df['Categoria'].str.upper().str.strip()

    # 2. Limpeza de títulos (Remove espaços extras que quebram filtros)
    df['Artigo'] = df['Artigo'].str.title().str.strip()

    print("\n✅ Dados normalizados para o Looker:")
    print(df.head())

    return df

if __name__ == "__main__":
    clean_marketing_data()
