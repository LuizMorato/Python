#“Todos os dias, nosso sistema atualiza as vendas do dia anterior. 
#O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, 
#assim que começar a trabalhar, com o faturamento e a quantidade de produtos no dia anterior”


#IDE: Jupyter (anaconda3)
import pandas
import pyautogui
import time
import pyperclip

# base de dados
tabela = pandas.read_excel(r"C:\Users\user\Downloads\Vendas - Dez.xlsx")
display(tabela)

faturamento = tabela["Valor final"].sum()
quantidade = tabela["Quantidade"].sum()

# abrir aba e entrar no e-mail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("link da empresa")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)
# clicar no botão escrever
pyautogui.click(x=1 y=1)
# preencher as informações do e-mail
pyautogui.write("destinatario@mail.com")
pyautogui.press("tab")
pyautogui.press("tab")
#assunto
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
#corpo
texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,..2f}
A quantidade de produtos foi de: {quantidade:,..2f}

Abs
LuizMorato"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
# clicar em enviar
pyautogui.hotkey("ctrl", "enter")