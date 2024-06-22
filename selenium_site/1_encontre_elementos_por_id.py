from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

botao = driver.find_element(By.ID, 'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')

if botao is not None:
    print('Botao found')
if botoes is not None:
    print('Botoes found')