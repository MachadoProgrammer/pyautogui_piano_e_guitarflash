from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', False, False)

# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(5)
# Rolar X quantidade em pixels(descer)
driver.execute_script("window.scrollTo(0, 1500);")
sleep(5)
# Rolar X quantidade em pixels(subir)
driver.execute_script("window.scrollTo(0, -1500);")
