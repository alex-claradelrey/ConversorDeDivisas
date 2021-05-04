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


Label(root, text="Valores Actuales:").place(x=20, y=10)

LabelBTC = Label(root, text="BTC:        - $")
LabelBTC.place(x=20, y=30)

LabelEURO = Label(root, text="EURO:     - $")
LabelEURO.place(x=20, y=50)

LabelLIBRA = Label(root, text="LIBRA:     - $")
LabelLIBRA.place(x=20, y=70)


divisas = ('Seleccione divisa...', 'BITCOIN (BTC)', 'EURO (EUR)', 'LIBRA (GBP)', 'DOLLAR (USD)')
divisa_seleccionada1 = tk.StringVar()
divisa_seleccionada2 = tk.StringVar()


combo_cb1 = ttk.Combobox(root, textvariable=divisa_seleccionada1, width=20)
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
    configuracion()
    LabelBTC.configure(text=f"BTC:      {btc_dollar()} $")
    LabelEURO.configure(text=f"EURO:   {euro_dollar()} $")
    LabelLIBRA.configure(text=f"LIBRA:  {libra_dollar()} $")
    combo_cb1.place(x=250, y=30)
    combo_cb2.place(x=250, y=90)
    LabelINFO.configure(text="Datos actualizados correctamente!")

messagebox.showinfo('Informacion', 'Al iniciarse la aplicacion\nespere a que se actualizen los datos')
root.after(500, datos)
root.mainloop()




