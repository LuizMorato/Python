#“Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, 
#entre os principais: internet e telefone.
#O problema é que, analisando o histórico dos clientes dos últimos anos, 
#você percebeu que a empresa está com Churn de mais de 26% dos clientes.
#Isso representa uma perda de milhões para a empresa.”

#IDE: Jupyter (anaconda3)
import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pandas.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
# - Entender as informações que você tem disponível
# - Descobrir as cagadas da base de dados
# axis -> 0 = linha; 1 = coluna

tabela = tabela.drop("coluna que quer apagar", axis = 1)
display(tabela)

# Passo 3: Tratamento de Dados
# - Resolver as "cagadas"

# Resolver os valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# A coluna em que TODOS os valores forem vazios, excluir, as linhas que tiverem valores nulos também.
tabela = tabela.dropna(how = "all", axis = 1)
# Resolver valores vazios
tabela = tabela.dropna(how = "any", axis = 1)

print(tabela.info())
# Passo 4: Análise Inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize = True).map("{"0.1%"}".format))
# value_counts = quantidade dos valores, sum = soma e mean = média

# Passo 5: Análise Detalhada - descobrir as causas do cancelamento
# Para edições nos gráficos: https://plotly.com/python/histograms/
# Cria o gráfico
# Para cada coluna na tabela, crie um gráfico
for coluna in tabela.columns:
		grafico = px.histogram(tabela, x = coluna, color = "Churn", text_auto = True)
#grafico de coluna = px.barplot, grafico de pizza = px.piechart
# Exibe o gráfico
		grafico.show()
