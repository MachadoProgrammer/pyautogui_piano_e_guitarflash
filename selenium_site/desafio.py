from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

# navegar ate o site
driver = iniciar_driver('https://cursoautomacao.netlify.app/desafios', True, False)
# encontrar e clicar em login
# sleep(5)
# botao_desafio = driver.find_element(By.LINK_TEXT, 'Desafios').click()
# sleep(3)
# campo_nome = driver.find_element(By.ID, 'dadosusuario').send_keys('Gabriel de Assis Machado')
# botao_cliqueAqui = driver.find_element(By.ID, 'desafio2').click()
driver.execute_script('scrollTo(0, 300)')
sleep(2)
# campo_input = driver.find_element(By.ID, 'escondido').send_keys('Gabriel')
# sleep(2)
# botao_validar = driver.find_element(By.ID, 'validarDesafio2').click()
driver.find_element(By.ID, 'conversivelcheckbox').click()
driver.find_element(By.ID, 'offroadcheckbox').click()
