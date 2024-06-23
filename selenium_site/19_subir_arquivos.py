from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import random
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

driver.execute_script("window.scrollTo(0, 2300);")
sleep(1)

escolher_arquivo = driver.find_element(By.XPATH, '//input[@id="myFile"]')
sleep(1)
escolher_arquivo.send_keys('C:\\DevAprender\\DevAprender\\PowerPyautoGui\\desafio\\excel.png')
sleep(2)
enviar_arquivo = driver.find_element(By.XPATH, '/html/body/section[7]/div/h3/form/input[2]')
enviar_arquivo.click()