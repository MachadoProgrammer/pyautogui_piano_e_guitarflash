from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import iniciar_driver

# ir até o Facebook
driver = iniciar_driver('https://www.facebook.com/?locale=pt_BR', True, False)
sleep(5)
# digitar o email
campo_email = driver.find_element(By.ID, 'email').send_keys('gabrieldiasmachado@gmail.com')
sleep(2)
# digitar a senha
campo_senha = driver.find_element(By.ID, 'pass').send_keys('M@rinha1215')
sleep(2)
# clicar em entrar
botao_entrar = driver.find_element(By.XPATH, '//button[@name="login"]').click()
sleep(8)
# encontrar e clicar no campo postagem
campo_postagem = driver.find_element(By.XPATH, '//span[text()="No que você está pensando, Gabriel?"]').click()
sleep(5)
# digitar algo
digitar_campo = driver.find_element(By.XPATH,
                                    '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
digitar_campo.click()
sleep(1)
digitar_campo.send_keys('Bom dia!')
# clicar em publicar
