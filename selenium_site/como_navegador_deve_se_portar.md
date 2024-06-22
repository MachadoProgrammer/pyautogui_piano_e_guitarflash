# Como alterar como o navegador deve se portar

## Fonte de opções de switches 
https://peter.sh/experiments/chromium-command-line-switches/?_gl=1*32t7rw*_ga*MzUyODg1MDYwLjE3MTM5MDg2OTM.*_ga_37GXT4VGQK*MTcxODkxNjUxOC41NC4xLjE3MTg5MjA5MDAuMC4wLjA.

## Standard configuration for chrome 
````
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
--incognito # Usar o modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada)
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU -> Virtual Machine
````

## A list of exerimental options (not all are documented)

https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc

## Standard configuration experimental features
````
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
    # notificar o google chrome sobre essa alteração
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,

})
````