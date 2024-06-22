from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

logo = driver.find_element(By.CLASS_NAME, 'navbar-brand')
links_menu = driver.find_elements(By.CLASS_NAME, 'nav-link')

if logo is not None:
    print('Found logo')
if links_menu is not None:
    print('Found links')