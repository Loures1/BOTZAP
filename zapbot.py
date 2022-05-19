from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://web.whatsapp.com/")

while len(driver.find_elements_by_id("side")) < 1:
    time.sleep(1)
        
        


