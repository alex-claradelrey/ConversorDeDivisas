from divisas import *

btc_dollar = btc_dollar()
euro_dollar = euro_dollar()
libra_dollar = libra_dollar()
#-----------
btc_euro = btc_euro()
dollar_euro = dollar_euro()
libra_euro = libra_euro()
#-----------
btc_libra = btc_libra()
euro_libra = euro_libra()
dollar_libra = dollar_libra()


def mostrarDivisas():
    return [btc_dollar, euro_dollar, libra_dollar]

def conversor2(divisa_ini, divisa_resul, cant):
    #btc a dollar, euro, libra
    if(divisa_ini == "BITCOIN (BTC)" and divisa_resul == "DOLLAR (USD)"):
        resul = cant * btc_dollar
        return resul
    elif(divisa_ini == "BITCOIN (BTC)" and divisa_resul == "EURO (EUR)"):
        resul = cant * btc_euro
        return resul
    elif(divisa_ini == "BITCOIN (BTC)" and divisa_resul == "LIBRA (GBP)"):
        resul = cant * btc_libra
        return resul
    #euro a btc, dollar, libra
    elif(divisa_ini == "EURO (EUR)" and divisa_resul == "BITCOIN (BTC)"):   
        resul = cant / btc_euro
        return resul
    elif(divisa_ini == "EURO (EUR)" and divisa_resul == "DOLLAR (USD)"):
        resul = cant / dollar_euro
        return resul
    elif(divisa_ini == "EURO (EUR)" and divisa_resul == "LIBRA (GBP)"):
        resul = cant / libra_euro
        return resul
    #libra a btc, euro, dollar
    elif(divisa_ini == "LIBRA (GBP)" and divisa_resul == "BITCOIN (BTC)"):
        resul = cant / btc_libra
        return resul
    elif(divisa_ini == "LIBRA (GBP)" and divisa_resul == "EURO (EUR)"):
        resul = cant / euro_libra
        return resul
    elif(divisa_ini == "LIBRA (GBP)" and divisa_resul == "DOLLAR (USD)"):
        resul = cant / dollar_libra
        return resul
    #dolar a btc, euro, libra
    elif(divisa_ini == "DOLLAR (USD)" and divisa_resul == "BITCOIN (BTC)"):
        resul = cant / btc_dollar
        return resul
    elif(divisa_ini == "DOLLAR (USD)" and divisa_resul == "EURO (EUR)"):
        resul = cant / euro_dollar
        return resul
    elif(divisa_ini == "DOLLAR (USD)" and divisa_resul == "LIBRA (GBP)"):
        resul = cant / libra_dollar
        return resul
    #dolar a dolar, euro  a euro, libra a libra, btc a btc para que no aparezca None
    elif(divisa_ini == "DOLLAR (USD)" and divisa_resul == "DOLLAR (USD)"):
        resul = cant
        return resul
    elif(divisa_ini == "EURO (EUR)" and divisa_resul == "EURO (EUR)"):
        resul = cant
        return resul
    elif(divisa_ini == "LIBRA (GBP)" and divisa_resul == "LIBRA (GBP)"):
        resul = cant
        return resul
    elif(divisa_ini == "BITCOIN (BTC)" and divisa_resul == "BITCOIN (BTC)"):
        resul = cant
        return resul

