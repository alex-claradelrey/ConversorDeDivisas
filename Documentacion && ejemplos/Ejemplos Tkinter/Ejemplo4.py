#bind y eventos

import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Devuelve la tecla presionada')


def log(event):
    print(event)


root = tk.Tk()

#captura la tecla enter del teclado
btn = ttk.Button(root, text='Guardar')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')


btn.focus()
btn.pack(expand=True)

root.mainloop()