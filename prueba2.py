import tkinter as tk

#declaracion
root = tk.Tk()

root.title("Esto es una prueba")

window_width = 700
window_height = 600

screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#para iniciar la interfaz
root.mainloop()


