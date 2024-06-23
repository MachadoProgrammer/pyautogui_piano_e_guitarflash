from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import random
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)
driver.save_screenshot('tela.jpg')
