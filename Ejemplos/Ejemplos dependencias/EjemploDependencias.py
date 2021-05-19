import os #necesitamos el modulo os de sistema para poder instalar las dependencias

#esta funcion se encarga de instalar los paquetes externos necesarios
#para la practica
def dependencias():
    #actualizamos el instalador de paquetes (encargado de instalar todos los paquetes que hay a continuacion)
    os.system('python -m pip install --upgrade pip') 
    #instalamos el paquete selenium (encargado de manejar el driver de google chrome para traer dicha informacion)
    os.system('pip install selenium') 
    #instalamos el paquete requests (encargado de hacer las peticiones de la pagina de google)
    os.system('pip install requests')
    #instalamos el paquete pillow (encargado de abrir las imagenes) 
    os.system('pip install pillow') 
