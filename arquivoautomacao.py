import pyautogui
import time 

pyautogui.PAUSE = 0.3       

pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")

time.sleep(5)  
pyautogui.write("file:///G:/documentos/Desktop/python/automacao%20python2/index.html")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=532, y=432)
pyautogui.write("testeautomacaopython@gmail.com")
pyautogui.press("tab") 
pyautogui.write("1234")
pyautogui.click(x=672, y=585) 
time.sleep(3)
 
# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=557, y=185)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
