from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from script.readexcel import Contatos, Grupos, Mensagem 
import time

def Bot():
    options = ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://web.whatsapp.com/")

    while len(driver.find_elements(By.XPATH, '//div[@id="side"]')) == False:
        time.sleep(1)

    time.sleep(6)

    if len(driver.find_elements(By.XPATH, '//*[@id="side"]')) == True:
        grupos = Grupos()
        pessoas = Contatos()
        mensagem = Mensagem()
        for grupo in grupos:
            element_nova_conversa = driver.find_element(By.XPATH, "//div[@class='_3yZPA']//div[2]//div[1]")
            element_nova_conversa.click()
            time.sleep(0.5)
            element_pesquisa = driver.find_element(By.XPATH, "//div[@title='Caixa de texto de pesquisa']")
            time.sleep(0.5)
            element_pesquisa.send_keys(grupo)
            time.sleep(1)
            element_grupo = driver.find_element(By.XPATH, f"//span[@title='{grupo}']")
            element_grupo.click()
            time.sleep(0.5)
            element_mensagem = driver.find_element(By.XPATH, f"//div[@title='Mensagem']")
            element_mensagem.click()
            pessoas_contatadas = [] 
            for pessoa in pessoas:
                element_mensagem.send_keys(f'@{pessoa}')
                time.sleep(0.5)
                element_mensagem.send_keys(Keys.TAB)
                time.sleep(0.5)
                element_marcacao = driver.find_elements(By.XPATH, f"//span[@class='copyable-text selectable-text']")
                if len(element_marcacao) == True:
                    element_mensagem.send_keys(mensagem['mensagem-grupo'])
                    time.sleep(0.5)
                    element_mensagem.send_keys(Keys.ENTER)
                    pessoas_contatadas.append(pessoa)
                    time.sleep(2)
                else:
                    element_mensagem.clear()
            for pessoa_contatada in pessoas_contatadas:
                pessoas.remove(pessoa_contatada)
        driver.close()
        return 'Concluido'


        