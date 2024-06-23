from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

# navegar ate o site
driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)
# encontrar e clicar em login
sleep(5)
botao_login = driver.find_element(By.LINK_TEXT, 'Login')
botao_login.click()
sleep(2)
# encontrar e digitar email e senha
campo_email = driver.find_element(By.ID, 'email')
campo_email.send_keys('gabrieldiasmachado@gmail.com')
sleep(2)
campo_senha = driver.find_element(By.ID, 'senha')
campo_senha.send_keys('123456')
sleep(1.5)
# clicar em entrar
botao_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
botao_enviar.click()