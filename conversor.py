
#todas las monedas basadas en dollar
dolar = 1
euro = 1.21
libra = 1.39
btc = 54379.40 
#las variables se actualizarán a tiempo real y se cambiarán

conversiones = {"dolar":dolar,"euro":euro,"libra":libra,"btc":btc} #dolares

def convertir_a_dollar(divisa,cant):
     resul = round(conversiones[divisa]*cant,3)
     return resul
    


def conversor(divisa_ini,divisa_resul,cant):
    if divisa_ini and divisa_resul in conversiones:
        if(divisa_ini =="dolar"):
           resul= round(conversiones[divisa_ini]*cant,3)+"$"
        else:
            cantDollar = convertir_a_dollar(divisa_ini,cant)
            resul =  round(cantDollar/conversiones[divisa_resul],3) 

            if(divisa_resul=="euro"):
                resul = str(resul)+"€"
            elif(divisa_resul=="libra"):
                resul = str(resul)+"£"
            elif(divisa_resul=="btc"):
                resul = str(resul)+"₿"
            
        return resul  
    else:
        print("error divisa no disponible")
      

print(conversor("euro","btc",10000))




