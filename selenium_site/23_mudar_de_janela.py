from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)

# Pegar a janela atual
janela_inicial = driver.current_window_handle

# Clicar no botão que abre uma nova janela
driver.execute_script('window.scrollTo(0, 500);')
sleep(3)

botao_janela = driver.find_element(By.XPATH, '//button[text()="Abrir Janela"]')
driver.execute_script('arguments[0].click();', botao_janela)

# Quais janelas estão abertas

janelas = driver.window_handles
for janela in janelas:
    if janela != janela_inicial:

        driver.switch_to.window()
        sleep(2)
        campo_pesquisa = driver.find_element(By.ID, 'campo_pesquisa')
        sleep(2)
        campo_pesquisa.send_keys('Curso de Automação')
        sleep(2)
        campo_pesquisar = driver.find_element(By.ID, 'fazer_pesquisa')
        campo_pesquisar.click()
        sleep(2)
        driver.close()

# Voltar para a janela inicial
driver.switch_to.window(janela_inicial)


