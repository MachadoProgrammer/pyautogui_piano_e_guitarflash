# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
import logging as lg

# Firefox -> geckodriver

lg.basicConfig(level=lg.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(message)s')


def iniciar_driver(site_url, detach=False, headless=False):
    lg.getLogger(__name__)
    try:
        chorme_options = Options()
        # Standard configuration for chrome
        '''
        --start-maximized # Inicia maximizado
        --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
        --incognito # Usar o modo anônimo
        --window-size=800,800 # Define a resolução da janela em largura e altura
        --headless # Roda em segundo plano(com a janela fechada)
        --disable-notifications # Desabilita notificações
        --disable-gpu # Desabilita renderização com GPU
        '''

        arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--disable-notifications']
        for argument in arguments:
            chorme_options.add_argument(argument)

        # configuracoes adicionais do options:

        # rodar em segundo plano
        if headless:
            chorme_options.add_argument('--headless')

        # manter janela aberta
        if detach:
            chorme_options.add_experimental_option('detach', True)

        # desabilitar pop-up de navegador controlado por automacao
        chorme_options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])

        # Using experimental settings
        chorme_options.add_experimental_option('prefs', {
            # Alterar o local padrão de ‘download’ de arquivos
            'download.default_directory': 'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\projetos '
                                          'pyautogui\\selenium_site',
            # notificar o Google chrome sobre essa alteração
            'download.directory_upgrade': True,
            # Desabilitar a confirmação de ‘download’
            'download.prompt_for_download': False,
            # Desabilitar notificações
            'profile.default_content_setting_values.notifications': 2,
            # Permitir multiplos downloads
            'profile.default_content_setting_values.automatic_downloads': 1,

        })

        # Initializing webdriver

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chorme_options)
        driver.get(site_url)

        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException,
                    TimeoutException
            ]
        )

        return driver, wait
    except Exception as e:
        lg.error(f'Error occurred while initializng driver: {type(e).__name__} - {e}')
        return None


if __name__ == '__main__':
    iniciar_driver('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal', detach=True)
