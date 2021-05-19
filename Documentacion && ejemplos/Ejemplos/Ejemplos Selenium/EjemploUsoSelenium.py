import EjemploDependenciasSelenium as driv #usare el ejemplo anterior para una demostracion de selenium
import os
import time



driver = driv.dependencia_driver()

#hare un ejemplo de tomar el tiempo actual de madrid (tiempo real)

""" lo primero que debemos hacer es crear una funcion para pasarle el enlace de la pagina
del tiempo y capturar los elements html para extrar los datos de dicha pagina y mostrarlos
por consola """


def recoger_tiempo():
    #comprobamos que el driver este ya disponible descargado
    if(os.path.isfile('chromedriver.exe')):
        #al driver le pasamos el enlace de la pagina de donde vamos a tomar los datos
        driver.get('https://www.google.com/search?q=tiempo+madrid&rlz=1C1CHZN_esES935ES935&sxsrf=ALeKk00m8OkygBG6kDICupI-63aY8R448Q%3A1621374652637&ei=vDakYPG6JpT_sAf-koGABg&oq=tiempo+madrid&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCAAjIECAAQQzICCAAyBQgAELEDMgQIABBDMgIIADICCAAyAggAMgUIABCxAzICCAA6BAgjECc6CggAELEDEIMBEEM6CAgAELEDEIMBOgYIIxAnEBM6BwgAEMkDEEM6BQgAEJIDOggIABCxAxDJA1CqE1jGKGCDKmgAcAJ4AIABmAGIAaEKkgEEMTAuNJgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwjxiN-hm9TwAhWUP-wKHX5JAGAQ4dUDCA4&uact=5')
        #marcamos un sleep de dos segundos para que cargue la pagina en segundo plano
        time.sleep(2)
        #creamos la variable tiempo en la cual guardaremos el elemento html
        tiempo = driver.find_element_by_xpath('//*[@id="wob_tm"]').text
        #dicho elemento ya ha sido capturado y se ha extraido el valor en formato de texto
        print(type(tiempo)) #devuelve str
        #ahora podemos mostrar por pantalla el tiempo actual o devolver el valor mediante un return
        return tiempo


resultado = recoger_tiempo()

print(resultado, "Grados celsius")
