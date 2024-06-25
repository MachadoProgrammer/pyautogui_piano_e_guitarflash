from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(1)
# Encontrar a iframe
iframe = driver.find_element(
    By.XPATH, "//iframe[@src='https://cursoautomacao.netlify.app/desafios.html']")

# Mudar para dentro da iframe
driver.switch_to.frame(iframe)
# Interagir com ela
campo_nome = driver.find_element(By.ID, 'dadosusuario')
campo_nome.send_keys('Machadex')
# Sair do iframe
driver.switch_to.default_content()
