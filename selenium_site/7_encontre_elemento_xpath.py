from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', False, False)

sections = driver.find_elements(By.XPATH, '/html/body/section')

if sections:
    print(f"Found {sections}")