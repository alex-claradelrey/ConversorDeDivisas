import os
import time
import requests
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuracion de las opciones del driver de google para usar selenium
options = Options()
# hacer que el driver trabaje en segundo plano con selenium
options.add_argument('--headless') #  evitar que abra una ventana de chrome sobre la cual trabajar 
options.add_argument('log-level=4') # evitar mensajes de advertencia e informacion innecesaria

    

def configuracionDriver():
    # En caso de que no exista, descargamos el driver de google chrome para poder trabajar con selenium
    if(os.path.isfile('chromedriver.exe')):
        print("->i Driver Listo para usarse")
    else:
        # Enlace de descarga del driver
        url = 'https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip'
        # Hacemos la peticion y permitimos que nos redirija
        req = requests.get(url, allow_redirects = True)
        # Abrimos dicho fichero de la peticion y lo escribimos en formato zip con escritura binaria para no perder datos.
        open('chromedriver_win32.zip', 'wb').write(req.content)

        # Descomprimimos el driver utilizando un modulo interno de Python lamado zipfile
        with zipfile.ZipFile('./chromedriver_win32.zip', 'r') as zip_ref:
            zip_ref.extractall('./')
        # Una vez extraido borramos el archivo .zip
        os.remove('chromedriver_win32.zip')

# Comprobamos que el driver ya esta descargado y existe
if(os.path.isfile('chromedriver.exe')):
    # Iniciamos el driver con la ruta del archivo.exe guardandolo en una variable
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
else:
    # En caso de que no exista y no lo encuentre se inicia la configuracion
    configuracionDriver()

# Saca el valor actual de la criptomoneda de Bitcoin - dolar basandose en google
def btc_dollar():
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=btc+dollar&oq=btc+dollar&aqs=chrome..69i57j0l4j0i10i433l2j0i10j0l2.1607j1j7&sourceid=chrome&ie=UTF-8')
        time.sleep(2)
        btc_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = btc_txt.replace('.', '')
        btc = aux.replace(',', '.')
        return float(btc)
    else:
        configuracionDriver()
        btc_dollar()

# Saca el valor actual del euro - dolar basandose en google
def euro_dollar():
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=euro+dollar&sxsrf=ALeKk013NH6_jkqMjykudAIz0EUTAqZ0ig%3A1619628422154&ei=hpGJYNz9COmFhbIPrKOa-AM&oq=euro+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQywEyBAgAEEMyBQgAEMsBMgUIABDLATIECAAQQzIGCAAQBxAeMgIIADICCAAyBQgAEMsBOgcIIxCxAhAnOgcIABAKEMsBOgQIABAKUJ3MP1jW1z9g1dk_aABwAngAgAGoAYgB3QSSAQMyLjOYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwjc2JSGsqHwAhXpQkEAHayRBj8Q4dUDCA4&uact=5')
        time.sleep(2)
        euro_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = euro_txt.replace('.', '')
        euro = aux.replace(',', '.')
        return float(euro)
    else:
        configuracionDriver()
        euro_dollar()

# Saca el valor actual de la libra - dolar basandose en google
def libra_dollar():
    if(os.path.isfile('chromedriver.exe')):
        driver.get('https://www.google.com/search?q=libra+dollar&sxsrf=ALeKk03c7cKLFrWpH3w8Psx6q2JBIFy6vg%3A1619629466496&ei=mpWJYOH9HciX8gLmpangDQ&oq=libra+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEAoyBQgAEMsBMggIABAHEAoQHjIGCAAQBxAeMgYIABAHEB4yCAgAEAcQChAeMgYIABAHEB4yBggAEAcQHjIICAAQBxAKEB4yBggAEAcQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQsQIQJzoKCAAQsQMQgwEQQzoECAAQQzoECAAQDVC7twpYx7wKYP6_CmgEcAJ4AIABeYgBmAWSAQM2LjGYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz&ved=0ahUKEwjhspL4taHwAhXIi1wKHeZSCtwQ4dUDCA4&uact=5')
        time.sleep(2)
        libra_txt = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        aux = libra_txt.replace('.', '')
        libra = aux.replace(',', '.')
        return float(libra)
    else:
        configuracionDriver()
        libra_dollar()
