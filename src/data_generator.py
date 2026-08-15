import numpy as np
import pandas as pd

from config import SEED

def data_generator (num_clientes):
    """
        Gera um dataframe com dados fictícios de clientes para análise de churn.
    """
    
    np.random.seed(SEED)
    
    #Variaveis
    fidelidade_meses = np.random.randint(1, 73, size = num_clientes)
    tipos_contratos_opts = ['Mensal', 'Anual', 'Dois_Anos']
    contratos_probs = [0.6, 0.25, 0.15]
    tipo_contrato = np.random.choice(tipos_contratos_opts,size = num_clientes, p = contratos_probs)
    serviço_internet_opts = ['Fibra Óptica', 'DSL', 'Não']
    internet_probs = [0.55, 0.35, 0.10]
    servico_internet = np.random.choice(serviço_internet_opts, size= num_clientes, p=internet_probs )
    
    fatura_base = {
        'Mensal': np.random.normal(60,20),
        'Anual' : np.random.normal(70,25),
        'Dois_Anos': np.random.normal(80,25)
    }
    
    fatura_mensal = [fatura_base[c] + fidelidade_meses[i] * 0.2 + np.random.normal(0,5) for i, c in enumerate(tipo_contrato)]
    fatura_mensal = np.clip(fatura_mensal, 20, 120)
    
    # Lógica para a probabilidade de Churn
    # Clientes com contrato mensal, baixa fidelidade e fatura alta têm maior chance de churn
    prob_churn_log = -2.5  # Intercepto base (tendência a não cancelar)
    prob_churn_log += -0.05 * fidelidade_meses  # Mais fidelidade, menor chance
    prob_churn_log += [3.0 if c == 'Mensal' else -1.5 if c == 'Anual' else -2.5 for c in tipo_contrato] # Contrato mensal aumenta muito a chance
    prob_churn_log += [0.8 if s == 'Fibra Óptica' else -0.5 for s in servico_internet] # Fibra tende a ter mais churn (talvez por preço)
    prob_churn_log += 0.03 * fatura_mensal # Fatura mais alta, mais chance
    
    # Converter log-odds para probabilidade usando a função sigmoide
    prob_churn = 1 / (1 + np.exp(-prob_churn_log))
    
    churn = np.random.binomial(1, prob_churn)
    
    df = pd.DataFrame({
        'ID_Cliente': range(1, num_clientes + 1),
        'Fidelidade_Meses': fidelidade_meses,
        'Tipo_Contrato': tipo_contrato,
        'Servico_Internet': servico_internet,
        'Fatura_Mensal': fatura_mensal,
        'Churn': churn
    })
    
    return df
        
    