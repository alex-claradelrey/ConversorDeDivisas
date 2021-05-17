import tkinter as tk


root = tk.Tk()
root.title('Ventana centrada')

window_width = 300
window_height = 200

#dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# busca la posicion de la pantalla de visualizacion
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# centra al pantalla
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.mainloop()