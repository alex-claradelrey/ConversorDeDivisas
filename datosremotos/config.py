import os # modulo os de sistema operativo para poder acceder a una funcion que comprueba que el fichero json existe en la ruta del proyecto
import json # modulo json para  convertir un diccionario en objeto json y escribirlo // y a la hora de leerlo volver a convertirlo a diccionario


 
def write(divisa="btc", cambio="euro"): # funcion es escritura del fichero json con la configuracion con valores por defecto btc (cryptomoneda bitcoin) y el cambio en euros
    config_divisas = { # diccionario con la configuracion
    "divisa": divisa,
    "cambio": cambio
    }

    json_escritura = json.dumps(config_divisas, indent=2) #  convierte el diccionario a objeto json
    with open("config.json", 'w') as outfile:
        outfile.write(json_escritura) # el objeto json es escrito en un fichero con extension .json


def read(): # funcion de lectura del fichero json con la configuracion 
    if(not os.path.isfile("config.json")): # este if comprueba si el fichero no existe crea uno con los datos por defecto
        print('->i Archivo de configuracion no encontrado, creando un por defecto...')
        write() # crea fichero por defecto
        print('->i Leyendo archivo...')
        with open('config.json','r') as openfile:
            json_lectura = json.load(openfile) # carga los datos del objeto json a formato diccionario
            return json_lectura # devuelve el fichero leido en formato diccionario
    else: # en caso de que exista lo lee y lo devuelve con un return
        print('->i Archivo de configuracion encontrado, leyendo...')
        with open('config.json','r') as openfile: # lee el fichero existente
            json_lectura = json.load(openfile) # carga los datos del objeto json a formato diccionario
            return json_lectura # devuelve el fichero leido en formato diccionario
