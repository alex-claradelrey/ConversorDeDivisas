
#todas las monedas basadas en dollar
# DOLAR es constante
dolar = 1
euro = 1.21 #$
libra = 1.39  #$
btc = 54379.40 #$ 
#las variables se actualizarán a tiempo real y se cambiarán

conversiones = {"dolar":dolar,"euro":euro,"libra":libra,"btc":btc} #dolares


def convertir_a_dollar(divisa,cant):
    '''
        RECIBE -> El nombre de una divisa y una cantidad
        DEVUELVE -> La cantidad convertida dollars
    '''
     resul = round(conversiones[divisa]*cant,3)
     return resul
    


def conversor(divisa_ini,divisa_resul,cant):
    '''
        RECIBE -> 
            divisa_ini :    La divisa que queremos convertir
            divisa_resul_ : La divisa a la que queremos convertir
            cant:           Cantidad que deseamos convertir
        DEVUELVE ->
            la cantidad convertida a la divisa especificada con 3 cifras significativa y formateada a string con su simbolo correspondiente    
    '''
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
      




