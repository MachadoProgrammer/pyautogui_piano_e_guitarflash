from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)


def select_checkbox(driver, checks):
    for check in checks:
        try:
            select_check = driver.find_element(*check)
            selected = "Selecionado" if select_check.is_selected() else select_check.click()
            print(f'O checkbox: {checks[1]} esta {selected}')
        except Exception as e:
            print(f'Error: {e}')


checks = [(By.ID, 'acessoNivel1Checkbox'),
          (By.ID, 'acessoNivel2Checkbox'),
          (By.ID, 'acessoNivel3Checkbox'), ]

select_checkbox(driver, checks)

input(' ')