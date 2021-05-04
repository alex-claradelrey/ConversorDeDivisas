import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# show the label here
foto = tk.PhotoImage(file='perrete.png').pack()
label = ttk.Label(
    root,
    text='KGB, putisimo amo del barrio',
    image = foto,
    compund ='top',
    font = ('Helvetica',14)
).pack(ipadx=10,ipady=10)


root.mainloop()