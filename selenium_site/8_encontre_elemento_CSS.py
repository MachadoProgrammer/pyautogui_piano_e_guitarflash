from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', False, False)

elemento = driver.find_element(By.CSS_SELECTOR, 'h3')
elementos = driver.find_element(By.CSS_SELECTOR, 'input[class="form-check-input"]')

if elemento:
    print("element")
if elementos:
    print("elementos")
