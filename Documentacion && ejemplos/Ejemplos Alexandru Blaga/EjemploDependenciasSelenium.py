import os # modulo os para comprobar que el driver ya esta descargado
import time # modulo time utilizado para hacer un sleep necesario
import zipfile # modulo zipfile necesario para descomprimir el driver de selenium
import requests # modulo request necesario para hacer la solicitud de descarga del driver de google
from selenium import webdriver #desde selenium importamos el webdriver
from selenium.webdriver.chrome.options import Options #tambien desde selenium importamos Options

#options se encarga de configurar de que forma queremos que selenium actue
""" 
En este caso hacemos que selenium oculte la ventana de google al consultar los datos
y que no muestre todos los eventos por consola que son innecesarios
"""
# Configuracion de las opciones del driver de google para usar selenium
options = Options()
# hacer que el driver trabaje en segundo plano con selenium
options.add_argument('--headless') #  evitar que abra una ventana de chrome sobre la cual trabajar 
options.add_argument('log-level=4') # evitar mensajes de advertencia e informacion innecesaria


def dependencia_driver():
    if(os.path.isfile('chromedriver.exe')): # comprueba si existe o no el driver para no perder tiempo descargandolo
        print('El driver ya existe, listo para usarse') #te notifica con un print

    else:
        print('->i Descargando driver...')
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
        print('->i Driver listo para usarse.')
    #devuelve el driver listo y configurado
    return webdriver.Chrome('./chromedriver.exe', options=options)

