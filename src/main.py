import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from config import NUM_CLIENTES
from data_generator import data_generator
from eda import eda

pd.set_option('display.float_format', lambda x: '%.4f' % x)

# ----- GERADOR DE DADOS -----
df_churn = data_generator(NUM_CLIENTES)

# ----- EDA -----
eda(df_churn)
