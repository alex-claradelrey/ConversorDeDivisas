import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# layout simple
root = tk.Tk()
root.geometry("300x200")
root.title('Registro')

# StringVar() se usa para indicar que se va a guardar un string en esa variable
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    cad = f'Tu email es: {email.get()} y tu contraseña: {password.get()}'
    showinfo(
        title='credenciales',
        message=cad
    )


# Registrarse
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# boton
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()