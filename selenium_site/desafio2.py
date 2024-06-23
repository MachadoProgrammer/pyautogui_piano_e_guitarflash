from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/desafios', True, False)
sleep(1)

inicial_window = driver.current_window_handle

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)

new_window = driver.find_element(By.XPATH, '//button[text()="Abrir nova janela"]')
driver.execute_script('arguments[0].click();', new_window)
sleep(1)

# Quais janelas estão abertas
windows_open = driver.window_handles
for windows in windows_open:
    if windows != inicial_window:
        driver.switch_to.window(windows)
        sleep(1)
        write = driver.find_element(By.ID, 'opiniao_sobre_curso')
        write.click()
        sleep(1)
        write.send_keys('Curso de Automação')
        sleep(1)
        search_button = driver.find_element(By.ID, 'fazer_pesquisa')
        search_button.click()
        sleep(1)
        

driver.switch_to.window(inicial_window)
sleep(1)
new_write = driver.find_element(By.ID, 'campo_desafio7')
sleep(1)
new_write.send_keys('Desafio 7')