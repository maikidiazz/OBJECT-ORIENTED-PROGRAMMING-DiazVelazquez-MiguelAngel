import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso Gamer | Lab 8")
        self.root.geometry("430x365")
        self.root.configure(bg="#EAF2F8")
        self.root.resizable(False, False)

        self.titulo = tk.Label(root, text="BIENVENIDO A GAME ACCESS",
                               font=("Arial", 17, "bold"), bg="#EAF2F8", fg="#154360")
        self.titulo.pack(pady=22)
        self.lbl_email = tk.Label(root, text="Tu correo electrónico:",
                                  font=("Arial", 11), bg="#EAF2F8")
        self.lbl_email.pack()
        self.entry_email = tk.Entry(root, width=34, font=("Arial", 11))
        self.entry_email.pack(pady=6)
        self.lbl_password = tk.Label(root, text="Tu contraseña:",
                                     font=("Arial", 11), bg="#EAF2F8")
        self.lbl_password.pack()
        self.entry_password = tk.Entry(root, width=34, font=("Arial", 11), show="*")
        self.entry_password.pack(pady=6)
        self.btn_login = tk.Button(root, text="Entrar a mi cuenta", width=21,
                                   bg="#2874A6", fg="white", font=("Arial", 11, "bold"), cursor="hand2")
        self.btn_login.pack(pady=15)
        self.btn_register = tk.Button(root, text="Registrarme", width=21,
                                      bg="#27AE60", fg="white", font=("Arial", 10), cursor="hand2")
        self.btn_register.pack()
        self.entry_email.focus_set()

    def obtener_datos(self):
        return self.entry_email.get().strip(), self.entry_password.get()

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)
