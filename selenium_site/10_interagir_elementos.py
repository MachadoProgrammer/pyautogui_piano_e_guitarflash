from selenium.webdriver.common.by import By
from app import iniciar_driver
from selenium.common.exceptions import NoSuchElementException

# Como saber se o elemento esta desabilitado

driver = iniciar_driver('https://cursoautomacao.netlify.app/desafios', False, False)

# def verificar_status(btn):
#     if btn.is_enabled():
#         print('Habilitado')
#     else:
#         print('Desabilitado')
#
#
# btn1 = driver.find_element(By.ID, 'btn1')
# btn2 = driver.find_element(By.CSS_SELECTOR, '.btn2.btn.btn-dark')
# btn3 = driver.find_element(By.CSS_SELECTOR, '.btn2.btn.btn-warning')
#
# verificar_status(btn1)
# verificar_status(btn2)
# verificar_status(btn3)


def verificar_status_e_imprimir(driver, seletores):
    for seletor in seletores:
        try:
            btn = driver.find_element(*seletor)
            status = 'Habilitado' if btn.is_enabled() else 'Desabilitado'
            print(f'Botão {seletor[1]} está {status}.')
        except NoSuchElementException:
            print(f'Botão {seletor[1]} não encontrado.')


# Lista de seletores dos botões a serem verificados
seletores = [
    (By.ID, 'btn1'),
    (By.CSS_SELECTOR, '.btn2.btn.btn-dark'),
    (By.CSS_SELECTOR, '.btn2.btn.btn-warning')
]

verificar_status_e_imprimir(driver, seletores)
