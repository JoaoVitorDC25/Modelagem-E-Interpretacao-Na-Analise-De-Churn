# Modelagem-E-Analise-De-Vendas

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Pandas](https://img.shields.io/badge/Pandas-2.3.2-purple) ![NumPy](https://img.shields.io/badge/NumPy-2.3.1-orange) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.5-red) ![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-green) ![Plotly](https://img.shields.io/badge/Plotly-6.3.0-yellow) ![Statsmodels](https://img.shields.io/badge/Statsmodels-0.14.5-gray) 

Este projeto tem como objetivo aplicar técnicas de análise estatística para identificar os principais  fatores  que  influenciam  o  churn  em  uma  empresa  fictícia  de  telecomunicações chamada Connecta Telecom. A partir de um conjunto de dados, o projeto conduz um processo completo  de  investigação,  desde  a  análise  exploratória  até  a  interpretação  dos  resultados obtidos com o modelo de Regressão Logística.

--- 
# Demonstração

O projeto realiza uma análise de Churn, buscando entender quais características dos clientes podem estar relacionadas ao cancelamento de um serviço.

O fluxo principal do projeto é:

Geração dos dados > Análise dos dados > Tratamento das informações > Modelagem estatística > Interpretação dos resultados

Durante a análise, são gerados gráficos para visualizar o comportamento dos clientes.

--- 

## Taxa de Churn Geral

![Taxa de Churn Geral](image/Taxa%20de%20Churn%20Geral.png)

---

## Taxa de Churn Por Contrato

![Taxa de Churn Por Contrato](/image/Taxa%20de%20Churn%20por%20Contrato.png)

---

## Distribuição da Fidelidade (em Meses) por Churn

![Distribuição da Fidelidade (em Meses) por Churn](image/Distribuição%20da%20Fidelidade%20(em%20Meses)%20por%20Churn.png)

---

## Distribuição da Fatura Mensal por Churn

![Distribuição da Fatura Mensal por Churn](image/Distribuição%20da%20Fatura%20Mensal%20por%20Churn.png)

---

# Tecnologias Utilizadas

- Python 3.11+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Statsmodels

---

# Estrutura do Projeto

```text
Modelagem-E-Interpretacao-Na-Analise-De-Churn/
│
├── images/
│
├── src/
│   ├── __init__.py
|   ├── chart.py
│   ├── config.py
│   ├── data_generator.py
│   ├── eda.py
|   ├── main.py
|   ├── preprocessing.py
│   └── statistic_modeling.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Como Executar
## 1. Clone o repositório

```bash
git clone https://github.com/JoaoVitorDC25/Modelagem-E-Interpretacao-Na-Analise-De-Churn
```

## 2. Acesse a pasta do projeto

```bash
cd Modelagem-E-Interpretacao-Na-Analise-De-Churn
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Execute a aplicação

```bash
python src/main.py
```

---

# Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

Principais bibliotecas utilizadas:

- pandas==2.3.2
- numpy==2.3.1
- matplotlib==3.10.5
- seaborn==0.13.2
- plotly==6.3.0
- statsmodels==0.14.5

---

# Conceitos Aplicados

Durante o desenvolvimento do projeto foram utilizados alguns conceitos importantes de análise de dados:

- Python: organização e desenvolvimento do projeto.
- Pandas: criação, tratamento e análise dos dados.
- NumPy: geração dos dados e cálculos matemáticos.
- Matplotlib, Seaborn e Plotly: criação dos gráficos.
- Análise Exploratória de Dados (EDA): compreensão do comportamento dos dados através de gráficos e estatísticas.
- Tratamento de dados: preparação das informações antes da análise.
- Variáveis Dummy: transformação de informações categóricas, como tipo de contrato, em valores que podem ser utilizados pelo modelo.
- Regressão Logística: utilizada para analisar a relação entre as características dos clientes e a ocorrência de Churn.
- Odds Ratio: utilizada para facilitar a interpretação da influência de cada variável sobre as chances de cancelamento.

O projeto busca demonstrar de forma prática como análise de dados e estatística podem ajudar a compreender os fatores relacionados ao Churn de clientes.

---

# Autor

**João Vitor Dias**
Técnico em Eletrônica • Estudante de Análise e Desenvolvimento de Sistemas

GitHub: https://github.com/JoaoVitorDC25

Linkedin: <https://www.linkedin.com/in/jo%C3%A3o-vitor-dias-14178a190/?skipRedirect=true>

### Áreas de interesse

-  Ciência de Dados
-  Inteligência Artificial
-  Visão Computacional
-  Desenvolvimento em Python

---

## Projeto em desenvolvimento

Este projeto integra meu portfólio de estudos em Python .
