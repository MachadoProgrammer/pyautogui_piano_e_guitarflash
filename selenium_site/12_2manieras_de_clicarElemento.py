from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)
sleep(2)
# Encontrar o elemento e depois interagir

botao = driver.find_element(By.ID, 'dropdownMenuButton')
# botao.click()


# Caso o metodo click nao funcione
driver.execute_script('arguments[0].click()', botao)
