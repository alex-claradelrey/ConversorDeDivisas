from tkinter import *
from PIL import ImageTk, Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


root = Tk()
root.geometry('800x800')
root.resizable(False, False)
root.title('Label Widget Image')

# display an image label
imagen = Image.open("perrete.png")
imagen = imagen.resize((512,512))
img = ImageTk.PhotoImage(imagen)

image_label = Label(
    root,
    image=img,
    text='Python',
    compound='top'
)
image_label.pack()

root.mainloop()

mainloop()