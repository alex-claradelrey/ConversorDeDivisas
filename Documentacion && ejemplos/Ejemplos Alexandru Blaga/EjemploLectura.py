import os

#lectura de un fichero
def lectura():
     # comprobamos que el fichero exista antes de intentar leerlo
    if(os.path.exists('lectura.txt')):
        # cada linea leida se guarda como fichero
        with open('lectura.txt', 'r') as fichero: 
            #leemos linea a linea y
            lineas = fichero.read()
            print(lineas) #imprimimos por pantalla
    else: #esto en caso de que no encuentre el fichero
        print('Error el fichero que intentas leer no existe')



lectura() #llamamos a la funcion leer fichero