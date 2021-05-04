from tkinter import *
from tkinter import ttk



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
btc_dollar = 0
ttk.Label(root, text="Valores Actuales:").place(x=20, y=10)
ttk.Label(root, text=f"BTC: {btc_dollar}$").place(x=20, y=30)

root.mainloop()