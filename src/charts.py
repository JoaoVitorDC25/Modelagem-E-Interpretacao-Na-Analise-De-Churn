import matplotlib.pyplot as plt

from config import FIGURE_SIZE, AZUL, LARANJA

plt.rcParams['figure.figsize'] = FIGURE_SIZE

def grafico_pie(titulo, dados):
    """
    Função para criar um gráfico de pizza
    """
    
    plt.pie(
      dados.values,
      labels = dados.index,
      autopct = '%1.2f%%',   # <-- Duas casas decimais
      startangle = 140, 
      colors = [AZUL, LARANJA],
      explode = [0.05 if label == 'Sim' else 0 for label in dados.index])

    plt.title(titulo, fontsize = 14)
    plt.show()