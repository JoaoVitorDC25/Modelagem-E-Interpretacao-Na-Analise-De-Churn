import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from config import NUM_CLIENTES
from data_generator import data_generator
from eda import eda
from preprocessing import preprocessing
from statistic_modeling import statistic_modeling

pd.set_option('display.float_format', lambda x: '%.4f' % x)

# ----- GERADOR DE DADOS -----
df_churn = data_generator(NUM_CLIENTES)

# ----- EDA -----
eda(df_churn)

# ----- PREPROCESSING -----
y, X = preprocessing(df_churn) 

# ----- MODELAGEM ESTATÌSTICA
statistic_modeling(y, X)


