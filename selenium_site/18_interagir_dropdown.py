from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import random
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/desafios', True, False)

# Importar uma funcinalionalidade so selenium qu permite trabalhar com select -> Interagir com os dropdrowns

# paises_dropdown = driver.find_element(By.XPATH, '//select[@id="paisesselect"]')
# opcoes = Select(paises_dropdown)
# #
# # # Maneiras de acessar
# # # Indice
# opcoes.select_by_index(1)
# # sleep(3)
# # # Value
# opcoes.select_by_value('africa')
# # sleep(3)
# # # texto de exibicao
# opcoes.select_by_visible_text('Chille')

# Desafio
driver.execute_script("window.scrollTo(0, 1950);")

paises_dropdown = driver.find_element(By.XPATH, '//select[@id="paisesselect"]')

opcoes = Select(paises_dropdown)
sleep(2)
opcoes.select_by_index(1)
sleep(3)
opcoes.select_by_value('africa')
sleep(3)
opcoes.select_by_visible_text('Chille')