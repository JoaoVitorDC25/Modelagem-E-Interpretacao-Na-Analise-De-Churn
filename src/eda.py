from charts import grafico_pie, grafico_barras_sns

def eda(df_churn):
    # Informações do dataframe
    print(f"\n ----- Informações do dataframe: ----- \n")
    df_churn.info()
    print(f"\n ----- Resumo Estatístico: ----- \n\n {df_churn.describe()}")
    print(f"\n ----- Resumo Estatístico das Variáveis Categóricas: ----- \n\n {df_churn.describe(include='object')}")
    
    # Taxa de churn
    churn_count = df_churn['Churn'].value_counts().rename(index = {1: 'Sim', 0: 'Não'})
    grafico_pie('Taxa de Churn Geral',churn_count)
    
    # Taxa de churn por contrato
    grafico_barras_sns('Taxa de Churn por Contrato', 
                       df_churn, 
                       '\n Tipo de contrato', 
                       'Número de Clientes',
                       'Churn (0=Não, 1=Sim)')