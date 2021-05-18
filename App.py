import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from divisas import *
from config import *
#from conversor import *
from conver import *
from PIL import ImageTk, Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True



root = Tk()

#centrar aplicacion en el centro de la pantalla

#medidas ventana aplicacion
app_ancho = 430
app_alto = 430

#sacar el ancho y alto del monitor
monitor_ancho = root.winfo_screenwidth()
monitor_alto = root.winfo_screenheight()

#marcar el punto central de la ventana
centro_x = int(monitor_ancho/2 - app_ancho/2)
centro_y = int(monitor_alto/2 - app_alto/2)

#fijamos dichas medidas
root.geometry(f'{app_ancho}x{app_alto}+{centro_x}+{centro_y}')

#fijamos titulo
root.title("Conversor de divisas")

#fijamos medidas fijas y no dejamos que se haga grande la ventana
root.resizable(False, False)

#colocamos los elementos

#variables
""" valor1 = DoubleVar()
valor2 = DoubleVar() """

Label(root, text="Valores a tiempo real:", font=("Arial",18), fg = '#0C7A90').place(x=20, y=10)

LabelBTC = Label(root, text="BTC-USD:     - $", font =("Helvetica",14))
LabelBTC.place(x=20, y=50)

LabelEURO = Label(root, text="EURO-USD:  - $", font =("Helvetica",14))
LabelEURO.place(x=20, y=80)

LabelLIBRA = Label(root, text="LIBRA-USD:  - $", font = ("Helvetica",14))
LabelLIBRA.place(x=20, y=110)


divisas = ('Seleccione divisa...', 'BITCOIN (BTC)', 'EURO (EUR)', 'LIBRA (GBP)', 'DOLLAR (USD)')
divisa_seleccionada1 = tk.StringVar()
divisa_seleccionada2 = tk.StringVar()

combo_cb1 = ttk.Combobox(root, textvariable=divisa_seleccionada1, width=15)  
combo_cb1['values'] = divisas
combo_cb1['state'] = 'readonly'
divisa = readDivisa()
combo_cb1.current(int(divisa['divisa']))

combo_cb2 = ttk.Combobox(root, textvariable=divisa_seleccionada2, width=15)
combo_cb2['values'] = divisas
combo_cb2['state'] = 'readonly'
cambio = readCambio()
combo_cb2.current(int(cambio['cambio']))

LabelINFO = Label(root, text="ESTADO: Actualizando datos online...")
LabelINFO.place(x=5, y=410)

def datos():
    """btc_dat = btc_dollar()
    euro_dat = euro_dollar()
    libra_dat = libra_dollar() """
    #aqui llama a un metodo del fichero conversor.py que actualiza los datos con los cuales vamos a hacer el cambio de divisa
    lista_divisas = mostrarDivisas()
    
    euro_dat = lista_divisas[0]
    libra_dat = lista_divisas[1]
    btc_dat = lista_divisas[2]

    LabelBTC.configure(text=f"BTC-USD:     {btc_dat} $")
    LabelEURO.configure(text=f"EURO-USD:  {euro_dat} $")
    LabelLIBRA.configure(text=f"LIBRA-USD:  {libra_dat} $")
    LabelINFO.configure(text="ESTADO: Datos actualizados correctamente!")

    combo_cb1.place(x=230, y=200)
    combo_cb2.place(x=230, y=260)

    valorLabel1 = Label(root, text="De... ").place(x=40, y=200)
    valorLabel2 = Label(root, text="A... ").place(x=40, y=260)



    #bindeo para la imagen
    combo_cb1.bind('<<ComboboxSelected>>', ponerImg_1)
    imgPorDefecto(360,180)
    combo_cb2.bind('<<ComboboxSelected>>', ponerImg_2)
    imgPorDefecto(360,240)

# cambios dejar como esta

    divisa_inicial = ttk.Entry(root)
    divisa_inicial.place(x=80, y=200)

    divisa_cambio = ttk.Entry(root)
    divisa_cambio.place(x=80, y=260)

    def convertir(event, divisa_inicial, divisa_cambio, combo_cb1, combo_cb2):

        resultado = conversor2(combo_cb1, combo_cb2, int(divisa_inicial.get()))
        print(resultado)
  
        divisa_cambio.delete(0, "")
        divisa_cambio.insert(0, str(resultado))
   


    btn_convertir = ttk.Button(root, text="Convertir")
    btn_convertir.place(x=100, y=300)
    btn_convertir.bind('<Button-1>', lambda event: convertir(event, divisa_inicial, divisa_cambio, combo_cb1.get(), combo_cb2.get()))



    
#genera las imagenes por defecto de los entry cuando inica con el "Seleccione divisa..."
def imgPorDefecto(equis, igriega):
    image = Image.open("imgs/exchange.png")
   
    # Reszie the image using resize() method
    resize_image = image.resize((50, 50))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.place(x=equis,y=igriega)   



def ponerImg_1(event):
    if(combo_cb1.get()=='BITCOIN (BTC)'):
        writeDivisa(1)
        image = Image.open("imgs/bitcoin.png")
    elif(combo_cb1.get()=='EURO (EUR)'):
        writeDivisa(2)   
        image = Image.open("imgs/euro.png")
    elif(combo_cb1.get()=='LIBRA (GBP)'):
        writeDivisa(3)
        image = Image.open("imgs/libra.png")
    elif(combo_cb1.get()=='DOLLAR (USD)'):
        writeDivisa(4)
        image = Image.open("imgs/dollar.png")
    else:
        writeDivisa(0)
        image = Image.open("imgs/exchange.png")
   
    # Reszie the image using resize() method
    resize_image = image.resize((50, 50))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.place(x=360,y=180)


def ponerImg_2(event):
    if(combo_cb2.get()=='BITCOIN (BTC)'):
        writeCambio(1)
        image = Image.open("imgs/bitcoin.png")
    elif(combo_cb2.get()=='EURO (EUR)'):
        writeCambio(2)   
        image = Image.open("imgs/euro.png")
    elif(combo_cb2.get()=='LIBRA (GBP)'):
        writeCambio(3)
        image = Image.open("imgs/libra.png")
    elif(combo_cb2.get()=='DOLLAR (USD)'):
        writeCambio(4)
        image = Image.open("imgs/dollar.png") 
    else:
        writeCambio(0)
        image = Image.open("imgs/exchange.png")
    # Reszie the image using resize() method
    resize_image = image.resize((50, 50))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.place(x=360,y=240)    



#aqui hacemos la funcion para conversion de divisas



#messagebox.showinfo('Informacion', 'Al iniciarse la aplicacion\nespere a que se actualizen los datos')
root.after(100, datos)
root.mainloop()