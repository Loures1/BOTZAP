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
        print('Aguardando Login')
        not_login = False
    
    time.sleep(1)

time.sleep(3)

if len(driver.find_elements(By.XPATH, '//*[@id="side"]')) == True:
    print('Logado')
    time.sleep(1)
    element_search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
    element_search.click()
    pessoa = 'Isa'
    element_search.send_keys(pessoa)
    time.sleep(1)
    element_contato = driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
    element_contato.click()