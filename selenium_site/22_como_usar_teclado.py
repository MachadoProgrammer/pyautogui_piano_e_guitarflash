from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

sleep(1)

botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
botao_windows.click()
botao_windows.send_keys(Keys.DOWN)
botao_windows.send_keys(Keys.TAB)
botao_windows.send_keys(Keys.PAGE_DOWN)
