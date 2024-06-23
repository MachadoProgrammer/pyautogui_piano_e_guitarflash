from selenium.webdriver.common.by import By
from time import sleep
import random
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/desafios', True, False)
# sleep(2)

# checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
# for check in checkboxes[:2]:
#     check.click()
driver.execute_script("window.scrollTo(0, 1600);")

carros = driver.find_elements(By.NAME, 'carros')

driver.execute_script('arguments[0].click()', carros[1])
driver.execute_script('arguments[0].click()', carros[3])
driver.execute_script('arguments[0].click()', carros[4])

sleep(3)
motos = driver.find_elements(By.NAME, 'motos')
driver.execute_script('arguments[0]', motos)
for moto in motos:
    moto.click()

