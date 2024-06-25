from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from time import sleep
from app import iniciar_driver

driver, wait = iniciar_driver('https://cursoautomacao.netlify.app/login', True, False)

# sugestoes_de_voo = wait.until(expected_conditions.visibility_of_all_elements_located(
#     (By.XPATH, "//div[@class='wIuJz']")))
# https://google.com/flights
# sugestoes_de_voo = wait.until(expected_conditions.visibility_of_any_elements_located(
#     (By.XPATH, "//div[@class='wIuJz']")))
#
# sugestoes_de_voo[0].click()
#
# sleep(5)

campo_email = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH, "//input[@id='email']")))
campo_email.send_keys('jhonatan@hotmail.com')
sleep(2)

campo_email.send_keys(Keys.TAB)

campo_senha = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH, '//input[@id="senha"]')))

campo_senha.send_keys('123456')

sleep(2)

campo_senha.send_keys(Keys.TAB)
campo_senha.send_keys(Keys.ENTER)

# submit = wait.until(expected_conditions.element_to_be_clickable(
#     (By.XPATH, '/html/body/section/form/div/button')
# ))
# submit.click()
