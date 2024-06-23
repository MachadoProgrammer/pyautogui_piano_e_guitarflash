from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', False, False)

linux = driver.find_element(By.ID, 'LinuxRadioButton')
if linux.is_selected():
    print("Botao ja selecionado")
else:
    linux.click()

# radio_button = driver.find_elements(By.XPATH, '//input[@type="radio"]')
# sleep(1)
# radio_button[1].click()