from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)
sleep(2)

driver.execute_script('window.scrollTo(0, 600);')
sleep(2)

driver.find_element(By.ID, 'nome').send_keys('Curso de Automação')
sleep(2)
botao_alerta = driver.find_element(By.ID, 'buttonalerta')
sleep(1)
botao_alerta.click()
sleep(1)
alerta1 = driver.switch_to.alert
alerta1.accept()
sleep(5)

botao_confirm = driver.find_element(By.ID, 'buttonconfirmar')
botao_confirm.click()
sleep(1)
alerta2 = driver.switch_to.alert
alerta2.dismiss()
sleep(2)

botao_prompt = driver.find_element(By.ID, 'botaoPrompt')
botao_prompt.click()
sleep(2)

alerta3 = driver.switch_to.alert
alerta3.send_keys('Machado')
sleep(2)
alerta3.accept()
sleep(2)
alerta3.dismiss()