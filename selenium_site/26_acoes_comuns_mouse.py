from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from app import iniciar_driver

# driver = iniciar_driver('https://cursoautomacao.netlify.app/exemplo_chains', True, False)

# actionChains(sequencia de passos)
driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)
# botao = driver.find_element(By.ID, 'botao-direito')
# chain = ActionChains(driver)
# chain.context_click(botao).pause(1).send_keys(Keys.DOWN).pause(1).send_keys(
#     Keys.DOWN).pause(1).send_keys(Keys.DOWN).pause(1).click().perform()


radio_button = driver.find_element(By.ID, 'WindowsRadioButton')
chain2 = ActionChains(driver)
chain2.click(radio_button).pause(1).send_keys(Keys.DOWN).pause(1).send_keys(Keys.UP).click().perform()