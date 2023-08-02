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
 

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=557, y=185)
    
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
  
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
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)
    
