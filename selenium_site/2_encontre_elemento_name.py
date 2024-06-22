from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

campo_nome = driver.find_element(By.NAME, 'seu-nome')
radio_buttons = driver.find_elements(By.NAME, 'exampleRadios')

if campo_nome is not None:
    print('Encontramos campo nome')
if radio_buttons is not None:
    print('encontramos os radio buttons')
