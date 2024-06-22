from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

link_home = driver.find_element(By.LINK_TEXT, 'Home')
partial_link = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Des')

if link_home is not None:
    print('link home encountered')
if partial_link is not None:
    print('partial link encountered')