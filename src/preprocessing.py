import pandas as pd
import statsmodels.api as sm

def preprocessing(data):
    print(f"\n ----- Dados Originais: ----- \n")
    print(data.head())
    print(f"\n ----- Categorias da variável Contrato: ----- \n")
    print(data.Tipo_Contrato.value_counts())
    print(f"\n ----- Categorias da variável Serviço: ----- \n")
    print(data.Servico_Internet.value_counts())

    #Variaveis dummy
    df_model=pd.get_dummies(data, columns = ['Tipo_Contrato','Servico_Internet'], drop_first=True, dtype=int)
    print(f"\n ----- Dados Processados: ----- \n")
    print(df_model.head())
    
    y = df_model['Churn']
    
    X = df_model.drop(['ID_Cliente', 'Churn'], axis=1)
    X = sm.add_constant(X)
    
    print(f"\n ----- Dados 'X' Preparados para o modelo: ----- \n")
    print(X.head())
    print(f"\n ----- Dados 'Y' Preparados para o modelo: ----- \n")
    print(y.head())
    
    return X, y

    
