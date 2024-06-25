from app import iniciar_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

# navegar ate o site
driver, wait = iniciar_driver(site_url='https://www.instagram.com/', detach=True, headless=False)

current_website = driver.current_window_handle


def written_by_hand(text, element):
    for word in text:
        element.send_keys(word)
        sleep(random.uniform(0.1, 0.2))


# encontrar o campo de email e digitar o email
email_acc = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
pass_acc = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
written_by_hand('gabrieldiasmach@gmail.com', email_acc)  # seu email
sleep(1)

# encontrar o campo de senha e digitar a senha
written_by_hand('M@rinha123', pass_acc)  # sua senha
sleep(1)
# clicar em entrar
pass_acc.send_keys(Keys.ENTER)
sleep(5)

while True:
    driver.get('https://instagram.com/devaprender')
    sleep(5)
    postagem = wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="_aagu"]')))
    sleep(3)
    postagem[0].click()
    sleep(3)

    try:
        verifica_curtida = driver.find_element(By.XPATH,
                                               '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div['
                                               '2]/div/article/div/div[2]/div/div/div[2]/section[1]//div['
                                               '@role="button"]//*[@aria-label="Curtir"]')
        sleep(86400)
    except:
        print('A imagem já havia sido curtida.')
    else:
        botao_curtir = driver.find_elements(By.XPATH,
                                            '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div['
                                            '2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]')
        sleep(5)
        driver.execute_script('arguments[0].click()', botao_curtir[0])
        print('Deu certo! A imagem acabou de ser curtida.')
        sleep(86400)


# try
#     save_info = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Salvar '
#                                                                        'informações"]')))
#     save_info.click()
# except wait as e:
#     print(f'Timeout waiting for the save information button: {e}')
# except wait as e:
#     print(f'Save information button not found: {e}')
# else:
#     pass
#
# sleep(4)

# Open a new tab
# # Open a new tab/window
# driver.execute_script("window.open('https://www.instagram.com/devaprender/', '_blank');")
#
# # Get all window handles (tabs)
# window_handles = driver.window_handles
#
# # Switch to the new tab (assuming it is the last opened tab)
# driver.switch_to.window(driver.window_handles[-1])
#
# # Now you can interact with the new tab
# # ...
#
# driver.close()
# https://pastecode.io/s/4gqj5n67?_gl=1*1va6dth*_ga*MzUyODg1MDYwLjE3MTM5MDg2OTM.*_ga_37GXT4VGQK*MTcxOTI2MjMzMi43Ni4xLjE3MTkyNjY1NjIuMC4wLjA.

# driver.switch_to.window(driver.window_handles[0])

# Navegar até a página alvo
# Clicar na última postagem
# Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs

# clicar em salvar info ou não
