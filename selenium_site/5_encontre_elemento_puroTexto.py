from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', False, False)

# //*[text()='texto aqui'] -> no inspect
titulo = driver.find_element(By.XPATH, "//*[text()='ZONA DE TESTES']")

if titulo:
    print(titulo.text)
