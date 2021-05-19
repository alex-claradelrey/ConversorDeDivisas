#Ejemplo Combo Box - Widgets
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# ventana
root = tk.Tk()
root.geometry('300x220')
root.resizable(False, False)
root.title('Radio Button Demo')


def show_selected_size():
    showinfo(
        title='Result',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('Rojo', 'rojo'),
         ('Azul', 'azul'),
         ('Verde', 'verde'),
         ('Amarillo', 'amarillo'),
         ('Rosa', 'rosa'))

# label
label = ttk.Label(text="Elige un color")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Elige color",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()