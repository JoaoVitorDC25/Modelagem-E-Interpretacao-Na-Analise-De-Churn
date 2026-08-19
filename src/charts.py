import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"


from config import FIGURE_SIZE, AZUL, LARANJA, TITLE_FONT_SIZE, PATH, DPI

plt.rcParams['figure.figsize'] = FIGURE_SIZE

def grafico_pie(titulo, data):
    """
    Função para criar um gráfico de pizza
    """
    
    plt.pie(
      data.values,
      labels = data.index,
      autopct = '%1.2f%%',   # <-- Duas casas decimais
      startangle = 140, 
      colors = [AZUL, LARANJA],
      explode = [0.05 if label == 'Sim' else 0 for label in data.index])

    plt.title(titulo, fontsize = TITLE_FONT_SIZE)
    
    plt.tight_layout()
    plt.savefig(PATH + titulo, dpi=DPI, bbox_inches='tight')
    plt.show()
  
def grafico_barras_sns(titulo, dado, xLabel, yLabel, legenda):
    """
    Função para criar gráfico de barras agrupadas, com Seaborn
    """
    sns.countplot(
      data=dado,
      x="Tipo_Contrato",
      hue="Churn",
      palette={0: AZUL, 1: LARANJA})
    
    plt.title(titulo, fontsize = TITLE_FONT_SIZE)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend(title=legenda)
    plt.xticks(rotation=0)
        
    plt.tight_layout()
    plt.savefig(PATH + titulo, dpi=DPI, bbox_inches='tight')
    plt.show()   
    
def grafico_histograma_inter(titulo, data):
  """
      Função para criar gráfico de histograma, com plotly
  """
  
  fig_hist_fidelidade = px.histogram(data, 
                                     x='Fidelidade_Meses', 
                                     color='Churn', 
                                     marginal='box',
                                     title=titulo, 
                                     labels={'Fidelidade_Meses':'Meses de Fidelidade'})
  
  fig_hist_fidelidade.write_image(PATH + titulo + ".png", format='png')# Salva a plotagem em /image
  fig_hist_fidelidade.show()
  