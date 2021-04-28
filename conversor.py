#todas las monedas basadas en dollar
dolar = 1
euro = 1.21
libra = 1.39
btn = 54379.40 

conversiones = {"dolar":dolar,"euro":euro,"libra":libra,"btn":btn} #dolares

def convertir_a_dollar(divisa,cant):
    return resul = round(conversiones[divisa]*cant,3)
    


def conversor(divisa_ini,divisa_resul,cant):
    if divisa_ini and divisa_resul in conversiones:
        if(divisa_ini =="dolar"):
           resul =  round(conversiones[divisa_ini]/cant,3)
        else:
               
    else:
        print("error divisa no disponible")
    return resul    


print(conversor("libra","euro",10))




