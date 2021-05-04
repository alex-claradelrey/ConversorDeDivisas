import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from datosremotos.conversor import *
from datosremotos.datosr import *
from datosremotos.config import *
from time import sleep


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
    width=20
)  

combo_cb1['values'] = divisas
combo_cb1['state'] = 'readonly'
combo_cb1.current(0)


combo_cb2 = ttk.Combobox(root, textvariable=divisa_seleccionada2, width=20)
combo_cb2['values'] = divisas
combo_cb2['state'] = 'readonly'
combo_cb2.current(0)




LabelINFO = Label(root, text="Actualizacion de datos...")
LabelINFO.place(x=5, y=410)

def configuracion():

    pass

def datos():
<<<<<<< HEAD

    if(os.path.isfile('./chromedriver.exe')):
        LabelBTC.configure(text=f"BTC:      {btc_dollar()} $")
        LabelEURO.configure(text=f"EURO:   {euro_dollar()} $")
        LabelLIBRA.configure(text=f"LIBRA:  {libra_dollar()} $")
        combo_cb1.place(x=250, y=30)
        combo_cb2.place(x=250, y=90)
        LabelINFO.configure(text="Datos actualizados correctamente!")
    else:
        configuracionDriver()
=======
    configuracion()
    LabelBTC.configure(text=f"BTC:      {btc_dollar()} $")
    LabelEURO.configure(text=f"EURO:   {euro_dollar()} $")
    LabelLIBRA.configure(text=f"LIBRA:  {libra_dollar()} $")
    combo_cb1.place(x=230, y= 200)
    valorLabel1 = Label(root,text="De...").place(x=45,y=200)
    valorLabel2 = Label(root,text="A...").place(x=45,y=240)
    combo_cb2.place(x=230, y= 240)
    LabelINFO.configure(text="Datos actualizados correctamente!")
    generarEntry(80,200,valor1)
    generarEntry(80,240,valor2)

def generarEntry(x,y,valor):
    valorEntry = Entry(root,textvariable = valor,show="")
    valorEntry.place(x=x,y=y)
    
>>>>>>> d5b5acbfff3ed7d272ee14a8f9f581fee10f37ce

messagebox.showinfo('Informacion', 'Al iniciarse la aplicacion\nespere a que se actualizen los datos')
root.after(5000, datos)
root.mainloop()




