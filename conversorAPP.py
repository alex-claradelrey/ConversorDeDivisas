import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from datosremotos.conversor import *
from datosremotos.datosr import *
from datosremotos.config import *
from time import sleep
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
valor1 = DoubleVar()
valor2 = DoubleVar()
Label(
    root, 
    text="Valores a tiempo real:",
    font=("Arial",18),
    fg = '#0C7A90'
).place(x=20, y=10)

LabelBTC = Label(
    root, 
    text="BTC:        - $",
    font =("Helvetica",14)
)
LabelBTC.place(x=20, y=50)

LabelEURO = Label(
    root, 
    text="EURO:     - $",
    font =("Helvetica",14)
)
LabelEURO.place(x=20, y=80)

LabelLIBRA = Label(
    root, 
    text="LIBRA:     - $",
    font = ("Helvetica",14)
)
LabelLIBRA.place(x=20, y=110)


divisas = ('Seleccione divisa...', 'BITCOIN (BTC)', 'EURO (EUR)', 'LIBRA (GBP)', 'DOLLAR (USD)')
divisa_seleccionada1 = tk.StringVar()
divisa_seleccionada2 = tk.StringVar()


combo_cb1 = ttk.Combobox(
    root, 
    textvariable=divisa_seleccionada1, 
    width=15
)  

combo_cb1['values'] = divisas
combo_cb1['state'] = 'readonly'
combo_cb1.current(0)


combo_cb2 = ttk.Combobox(root, textvariable=divisa_seleccionada2, width=15)
combo_cb2['values'] = divisas
combo_cb2['state'] = 'readonly'
combo_cb2.current(0)




LabelINFO = Label(root, text="Actualizacion de datos...")
LabelINFO.place(x=5, y=410)

def configuracion():

    pass

def datos():

    if(os.path.isfile('./chromedriver.exe')):
        LabelBTC.configure(text=f"BTC:      {btc_dollar()} $")
        LabelEURO.configure(text=f"EURO:   {euro_dollar()} $")
        LabelLIBRA.configure(text=f"LIBRA:  {libra_dollar()} $")
        combo_cb1.place(x=250, y=30)
        combo_cb2.place(x=250, y=90)
        LabelINFO.configure(text="Datos actualizados correctamente!")
    else:
        configuracionDriver()
    configuracion()
    LabelBTC.configure(text=f"BTC:      {btc_dollar()} $")
    LabelEURO.configure(text=f"EURO:   {euro_dollar()} $")
    LabelLIBRA.configure(text=f"LIBRA:  {libra_dollar()} $")
    combo_cb1.place(x=230, y= 200)
    valorLabel1 = Label(root,text="De...").place(x=40,y=200)
    valorLabel2 = Label(root,text="A...").place(x=40,y=260)
    combo_cb2.place(x=230, y= 260)

    #bindeo para la imagen
    combo_cb1.bind('<<ComboboxSelected>>', ponerImg)
    combo_cb2.bind('<<ComboboxSelected>>', ponerImg2)

    LabelINFO.configure(text="Datos actualizados correctamente!")
    generarEntry(80,200,valor1)
    generarEntry(80,260,valor2)
    generarButton(100,300)

def ponerImg(event):
    if(combo_cb1.get()=='BITCOIN (BTC)'):
        image = Image.open("imgs/bitcoin.png")
    elif(combo_cb1.get()=='EURO (EUR)'):   
        image = Image.open("imgs/euro.png")
    elif(combo_cb1.get()=='DOLLAR (USD)'):
        image = Image.open("imgs/dollar.png")
    elif(combo_cb1.get()=='LIBRA (GBP)'):
        image = Image.open("imgs/libra.png")
    else:
        image = Image.open("imgs/exchange.png")
   
    # Reszie the image using resize() method
    resize_image = image.resize((50, 50))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.place(x=360,y=180)


def ponerImg2(event):
    if(combo_cb2.get()=='BITCOIN (BTC)'):
        image = Image.open("imgs/bitcoin.png")
    elif(combo_cb2.get()=='EURO (EUR)'):   
        image = Image.open("imgs/euro.png")
    elif(combo_cb2.get()=='DOLLAR (USD)'):
        image = Image.open("imgs/dollar.png")
    elif(combo_cb2.get()=='LIBRA (GBP)'):
        image = Image.open("imgs/libra.png") 
    else:
        image = Image.open("imgs/exchange.png")
    # Reszie the image using resize() method
    resize_image = image.resize((50, 50))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.place(x=360,y=240)    
        

def generarEntry(x,y,valor):
    valorEntry = Entry(root,textvariable = valor,show="")
    valorEntry.place(x=x,y=y)
def generarButton(x,y):
    boton = Button(
        root,
        text="Enviar"
    ).place(x=x,y=y)


messagebox.showinfo('Informacion', 'Al iniciarse la aplicacion\nespere a que se actualizen los datos')
root.after(5000, datos)
root.mainloop()




