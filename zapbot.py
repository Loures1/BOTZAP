from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://web.whatsapp.com/")
not_login = True 

while len(driver.find_elements(By.XPATH, '//*[@id="side"]')) == False:
    if not_login == True:
        not_login = False
    
    time.sleep(1)

time.sleep(6)

if len(driver.find_elements(By.XPATH, '//*[@id="side"]')) == True:
    grupo = 'amigos e bonaza'
    pessoa = 'Newzinho'
    time.sleep(1)
    element_search = driver.find_element(By.XPATH, "//div[@title='Caixa de texto de pesquisa']")
    element_search.click()
    element_search.send_keys(pessoa)
    time.sleep(1)
    element_contato = driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
    element_contato.click()
    time.sleep(1)
    element_mensagem = driver.find_element(By.XPATH, f"//div[@title='Mensagem']")
    element_mensagem.click()
    element_mensagem.send_keys('.')
    time.sleep(1)
    element_mensagem.send_keys(Keys.ENTER)
    time.sleep(2)
    element_search.send_keys(grupo)
    time.sleep(1)
    element_contato = driver.find_element(By.XPATH, f"//span[@title='{grupo}']")
    element_contato.click()
    time.sleep(1)
    element_mensagem = driver.find_element(By.XPATH, f"//div[@title='Mensagem']")
    element_mensagem.send_keys(f'@{pessoa}')
    time.sleep(1)
    element_mensagem.send_keys(Keys.TAB)
    element_mensagem.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.close()



