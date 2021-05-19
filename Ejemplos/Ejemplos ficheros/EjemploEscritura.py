# importamos el modulo os de sistema para poder comprobar si el fichero a escribir ya existe
import os


def escritura(texto): # funcion que escribe ficheros de texto en el sistema
    if(os.path.exists('escritura.txt')): #primero comprobamos que el fichero no exista
        print('fichero existente!') #en caso de existir salta este print
    else:
        #aqui escribimos el fichero de tipo texto 
        with open('escritura.txt', 'w') as fichero: 
            fichero.write(texto) #escribe cada linea



#texto a guardar en fichero
txt = """
esto es un texto
multi linea para comprobar

que no solo escribe lineas simples
""" 

escritura(txt) #llamamos a la funcion pasandole el parametro