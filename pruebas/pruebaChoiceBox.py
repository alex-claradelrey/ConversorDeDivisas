import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from PIL import ImageTk, Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')


def month_changed(event):
    msg = f'You selected {month_cb.get()}!'
    showinfo(title='Result', message=msg)
def ponerImg(event):
    if(month_cb.get()=='Btc'):
        image = Image.open("bitcoin.png")
    elif(month_cb.get()=='euro'):   
        image = Image.open("euro.png")
    elif(month_cb.get()=='dollar'):
        image = Image.open("dollar.png")
    else:
        image = Image.open("libra.png")   
    # Reszie the image using resize() method
    resize_image = image.resize((50, 50))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.place(x=200,y=50)
        

# month of year
months = ('Btc','euro','dollar','libra')    

label = ttk.Label(text="Please select a month:")
label.pack(fill='x', padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()

month_cb = ttk.Combobox(root, textvariable=selected_month)
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.place(x=10,y=10)




month_cb.bind('<<ComboboxSelected>>', ponerImg)

root.mainloop()