from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from readexcel import Contatos, Grupos, Mensagem 
import time

options = ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://web.whatsapp.com/")
not_login = True 

while len(driver.find_elements(By.XPATH, '//div[@id="side"]')) == False:
    if not_login == True:
        not_login = False
    
    time.sleep(1)

time.sleep(6)

if len(driver.find_elements(By.XPATH, '//*[@id="side"]')) == True:
    grupos = Grupos()
    pessoas = Contatos()
    mensagem = Mensagem()
    for pessoa in pessoas:
        element_search = driver.find_element(By.XPATH, "//div[@title='Caixa de texto de pesquisa']")
        element_search.click()
        element_search.send_keys(pessoa)
        time.sleep(1)
        element_contato = driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
        for grupo in grupos:
            element_grupo = driver.find_elements(By.XPATH, f"//div[@class='_2nY6U vq6sj']//span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr'][contains(text(),'{grupo}')]")
            if len(element_grupo) == 1:
                nome_grupo = grupo
                break        
        element_contato.click()
        time.sleep(1)
        element_mensagem = driver.find_element(By.XPATH, f"//div[@title='Mensagem']")
        element_mensagem.click()
        element_mensagem.send_keys(mensagem['mensagem'])
        element_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)
        element_search.click()
        element_search.send_keys(nome_grupo)
        time.sleep(1)
        element_grupo = driver.find_element(By.XPATH, f"//span[@title='{grupo}']")
        element_grupo.click()
        time.sleep(1)
        element_mensagem = driver.find_element(By.XPATH, f"//div[@title='Mensagem']")
        element_mensagem.click()
        element_mensagem.send_keys(f'@{pessoa}')
        element_mensagem.send_keys(Keys.TAB)
        element_mensagem.send_keys(mensagem['mensagem-grupo'])
        element_mensagem.send_keys(Keys.ENTER)
        time.sleep(3)
    driver.close()


