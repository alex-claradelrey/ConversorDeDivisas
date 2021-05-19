import os
import json


def writeDivisa(divisa=0):
    config_divisa = {
        "divisa": divisa
    }
    json_escritura = json.dumps(config_divisa, indent=1)
    with open('config_divisa.json', 'w') as salida_fich:
        salida_fich.write(json_escritura)

def writeCambio(cambio=0):
    config_cambio = {
        "cambio": cambio
    }
    json_escritura = json.dumps(config_cambio, indent=1)
    with open('config_cambio.json', 'w') as salida_fich:
        salida_fich.write(json_escritura)


def readDivisa():
    if(not os.path.isfile('config_divisa.json')):
        print('->i Archivo de configuracion no encontrado, creando un por defecto...')
        writeDivisa() # crea fichero por defecto
        print('->i Leyendo archivo...')
        with open('config_divisa.json','r') as openfile:
            json_lectura = json.load(openfile) # carga los datos del objeto json a formato diccionario
            return json_lectura # devuelve el fichero leido en formato diccionario
    else: # en caso de que exista lo lee y lo devuelve con un return
        print('->i Archivo de configuracion encontrado, leyendo...')
        with open('config_divisa.json','r') as openfile: # lee el fichero existente
            json_lectura = json.load(openfile) # carga los datos del objeto json a formato diccionario
            return json_lectura # devuelve el fichero leido en formato diccionario

def readCambio():
    if(not os.path.isfile('config_cambio.json')):
        print('->i Archivo de configuracion no encontrado, creando un por defecto...')
        writeCambio() # crea fichero por defecto
        print('->i Leyendo archivo...')
        with open('config_cambio.json','r') as openfile:
            json_lectura = json.load(openfile) # carga los datos del objeto json a formato diccionario
            return json_lectura # devuelve el fichero leido en formato diccionario
    else: # en caso de que exista lo lee y lo devuelve con un return
        print('->i Archivo de configuracion encontrado, leyendo...')
        with open('config_cambio.json','r') as openfile: # lee el fichero existente
            json_lectura = json.load(openfile) # carga los datos del objeto json a formato diccionario
            return json_lectura # devuelve el fichero leido en formato diccionario

