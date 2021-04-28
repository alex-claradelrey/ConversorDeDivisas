import os
import time
import requests
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def config():
    # Configuracion de las opciones del driver de google para usar selenium
    options = Options()
    # hacer que el driver trabaje en segundo plano con selenium
    options.add_argument('--headless') #  evitar que abra una ventana de chrome sobre la cual trabajar 
    options.add_argument('log-level=3') # evitar mensajes de advertencia e informacion innecesaria

    # En caso de que no exista, descargamos el driver de google chrome para poder trabajar con selenium
    if(os.path.isfile):
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

