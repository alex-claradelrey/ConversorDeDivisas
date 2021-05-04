import tkinter as tk;
from tkinter import ttk;
'''
def button_clicked(args):
    print(args)
def numero():
    return 2
'''
def select(option):
    print(option)
root = tk.Tk()

'''
 declaración sencilla
 button = ttk.Button(root,text='Click me',comman=button_clicked).place(x=10;y=10)

'''
ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()