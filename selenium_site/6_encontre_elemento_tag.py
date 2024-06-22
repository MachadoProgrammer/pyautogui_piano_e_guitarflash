from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', False, False)

titulo_do_site = driver.find_element(By.TAG_NAME, 'img')
elementos_h4 = driver.find_elements(By.TAG_NAME, 'h4')

if titulo_do_site:
    print('Encontrei o título do site')
if elementos_h4:
    print('Encontrei os elementos h4')