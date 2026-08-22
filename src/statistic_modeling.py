import statsmodels.api as sm
import numpy as np

def statistic_modeling(y, X):
    
    modelo = sm.Logit(y, X)

    #print(type(modelo))

    modelo_treinado = modelo.fit()
    
    print(modelo_treinado.summary())
    
    #Razão de Odds
    params = modelo_treinado.params
    conf = modelo_treinado.conf_int()
    conf['Odds Ratio'] = params
    conf.columns = ['2.5%', '97,5%', 'Odds Ratio']
    conf = np.exp(conf)
    
    print(conf)
    
    