from selenium.webdriver.common.by import By
from time import sleep
from app import iniciar_driver

driver = iniciar_driver('https://cursoautomacao.netlify.app/', True, False)
sleep(1)
driver.execute_script("window.scrollTo(0, 1600);")
sleep(1)
imagens = driver.find_elements(By.XPATH, '//img[@class="img-thumbnail"]')
sleep(1)
contador = 1
for imagem in imagens:
    with open(f'imagem{contador}.png', 'wb') as f:
        f.write(imagem.screenshot_as_png)
        sleep(1)

    contador += 1
