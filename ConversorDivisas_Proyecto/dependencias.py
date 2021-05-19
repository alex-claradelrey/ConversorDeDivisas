import os
import time
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuracion de las opciones del driver de google para usar selenium
options = Options()
# hacer que el driver trabaje en segundo plano con selenium
options.add_argument('--headless') #  evitar que abra una ventana de chrome sobre la cual trabajar 
options.add_argument('log-level=4') # evitar mensajes de advertencia e informacion innecesaria



#primero instala las dependencias de modulos externos
def dep_paquetes():
    os.system('python -m pip install --upgrade pip') #actualizamos el instalador de paquetes (encargado de instalar todos los paquetes que hay a continuacion)
    os.system('pip install selenium') #instalamos el paquete selenium (encargado de manejar el driver de google chrome para traer dicha informacion)
    os.system('pip install requests') #instalamos el paquete requests (encargado de hacer las peticiones de la pagina de google)
    os.system('pip install pillow') #instalamos el paquete pillow (encargado de abrir las imagenes)

#################################################################

#segundo instalamos el driver de google chrome necesario para usar selenium

def dep_driver():
    if(os.path.isfile('chromedriver.exe')):
        print("->i Driver listo para usarse.")
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
    return webdriver.Chrome('./chromedriver.exe', options=options)

#################################################################

