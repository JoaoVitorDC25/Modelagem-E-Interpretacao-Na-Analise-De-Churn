def eda(df_churn):
    # Informações do dataframe
    print(f"\n ----- Informações do dataframe: ----- \n")
    df_churn.info()
    print(f"\n ----- Resumo Estatístico: ----- \n\n {df_churn.describe()}")
    print(f"\n ----- Resumo Estatístico das Variáveis Categóricas: ----- \n\n {df_churn.describe(include='object')}")
    