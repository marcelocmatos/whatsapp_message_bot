import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos = pd.read_excel('contatos.xlsx', sheet_name='Contatos')

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')
while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos['MENSAGEM']):
    pessoa = contatos.loc[i, 'NOME']
    numero = contatos.loc[i, 'TELEFONE']
    texto = urllib.parse.quote(mensagem)
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
    navegador.get(link)
    while len(navegador.find_elements_by_id('side')) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(20)