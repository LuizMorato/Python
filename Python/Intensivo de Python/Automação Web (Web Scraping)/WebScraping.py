#“Trabalharemos em uma importadora e o preço dos nossos produtos é vinculado a cotação de

#- Dólar
#- Euro
#- Ouro

#Precisamos pegar na internet, de forma automática, 
#a cotação desses 3 itens e saber quanto demos cobrar pelos nossos produtos, 
#considerando uma margem de contribuição de termos na nossa base de dados.”

#Para isso, vamos criar uma automação web:

#- Selenium
#- Importante: baixar o webdriver

#IDE: JUPYTER (anaconda3)
#!pip install selenium
# baixar na pasta do python
# Chrome -> chromedriver Versão 108.0.5359.125
# Firefox -> geckodriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

# Passo 1: Pegar a cotação do dólar
#entrar no google
navegador.get("https://www.google.com/")

#XPATH: identifica os elementos de um site.
navegador.find_element('xpath', '//*[@id="input"]').send_keys("cotação dólar")
#.click() para clicar nele, .get() parapegar informação e .send_keys() escrever
navegador.find_element('xpath', '//*[@id="input"]').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Passo 2: Pegar a cotação do euro

navegador.get("https://www.google.com/")
navegador.find_element('xpath', '//*[@id="input"]').send_keys("cotação euro")
navegador.find_element('xpath', '//*[@id="input"]').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Passo 3: Pegar a cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
navegador.quit()
# Passo 4: Atualizar a base
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

# Passo 5: Recalcular os preços
#-atualizar a cotação
tabela.loc[tabela["Moeda"] == "Dolár", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Dolár", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Dolár", "Cotação"] = float(cotacao_ouro)
#-preço de compra = cotação * preço original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
#-preço de venda = preço de compra * margem 
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R$(:.2f)".format)
# Passo 6: Exportar a base atualizada
tabela.to_excel("Produtos Novo.xlsx")

