#argumentos funciones en Tkinter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def select(opcion):
    print(opcion)


ttk.Button(root, text='hola', command=lambda: select('hola')).pack()
ttk.Button(root, text='mundo',command=lambda: select('mundo')).pack()


root.mainloop()