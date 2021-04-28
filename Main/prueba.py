from tkinter import *
from tkinter import ttk
#define ventana principal

def saludo():
    raiz2 = Tk()
    raiz2.geometry('300x200')
    
    entrada = ttk.Entry(raiz2);
    entrada.place(x=50,y=50)

    
    ttk.Label(raiz2,text="saludame esta").pack(side=BOTTOM)

raiz = Tk()

raiz.geometry('300x200')
raiz.configure(bg = 'beige')
raiz.title('Aplicacion')

ttk.Button(raiz,text='saludame',command=saludo).pack(side=BOTTOM)

raiz.mainloop()