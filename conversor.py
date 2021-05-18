from divisas import *
#todas las monedas basadas en dollar
# DOLAR es constante
dolar = 1
euro = euro_dollar()
libra = libra_dollar()
btc = btc_dollar()
#faltan divisas 

def actualizarDivisas():
    return [euro, libra, btc]

#las variables se actualizarán a tiempo real y se cambiarán
conversiones = {"DOLLAR (USD)":dolar,"EURO (EUR)":euro,"LIBRA (GBP)":libra,"BITCOIN (BTC)":btc} #dolares
print(euro)
def convertir_a_dollar(divisa, cant):
    '''
        RECIBE -> El nombre de una divisa y una cantidad
        DEVUELVE -> La cantidad convertida en dollars
    '''

    resul = round(conversiones[divisa]*cant,3)
    return resul


def conversor(divisa_ini, divisa_resul, cant):
    if divisa_ini and divisa_resul in conversiones:
        if(divisa_ini == "DOLLAR (USD)"):
            resul = round(conversiones[divisa_ini]*cant, 3)
        else:
            cantDollar = convertir_a_dollar(divisa_ini, cant)
            resul = round(cantDollar/conversiones[divisa_resul], 3)

            if(divisa_resul=="EURO (EUR)"):
                resul = str(resul)+"€"
            elif(divisa_resul=="LIBRA (GBP)"):
                resul = str(resul)+"£"
            elif(divisa_resul=="BITCOIN (BTC)"):
                resul = str(resul)+"₿"

        return resul
    else:
        print("error divisa no disponible")