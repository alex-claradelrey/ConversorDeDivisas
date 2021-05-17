from tkinter import Tk, Text

#Text genera una pantalla de texto multilinea en otros lenguajes en un textarea
root = Tk()
root.geometry("250x200")
root.resizable(False, False)
root.title("Escribe aquí")

text = Text(root, height=8)
text.pack()

#insert(linea donde queremos que se ubique el texto, texto)
text.insert("1.0","Estamos aprendiendo python")


root.mainloop()
