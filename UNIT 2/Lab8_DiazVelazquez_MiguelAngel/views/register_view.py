import tkinter as tk
from tkinter import messagebox


class RegisterView:
    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Game Access | Crear cuenta")
        self.ventana.geometry("430x450")
        self.ventana.configure(bg="#E8F8F5")
        self.ventana.resizable(False, False)
        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(self.ventana, text="ÚNETE A GAME ACCESS",
                               font=("Arial", 17, "bold"), bg="#E8F8F5", fg="#117864")
        self.titulo.pack(pady=18)
        self.lbl_nombre = tk.Label(self.ventana, text="¿Cómo te llamas?", bg="#E8F8F5", font=("Arial", 10))
        self.lbl_nombre.pack()
        self.entry_nombre = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entry_nombre.pack(pady=5)
        self.lbl_email = tk.Label(self.ventana, text="Correo electrónico:", bg="#E8F8F5", font=("Arial", 10))
        self.lbl_email.pack()
        self.entry_email = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entry_email.pack(pady=5)
        self.lbl_password = tk.Label(self.ventana, text="Crea una contraseña:", bg="#E8F8F5", font=("Arial", 10))
        self.lbl_password.pack()
        self.entry_password = tk.Entry(self.ventana, width=35, show="*", font=("Arial", 10))
        self.entry_password.pack(pady=5)
        self.lbl_confirmar = tk.Label(self.ventana, text="Repite tu contraseña:", bg="#E8F8F5", font=("Arial", 10))
        self.lbl_confirmar.pack()
        self.entry_confirmar = tk.Entry(self.ventana, width=35, show="*", font=("Arial", 10))
        self.entry_confirmar.pack(pady=5)
        self.btn_guardar = tk.Button(self.ventana, text="Crear mi cuenta", width=22,
                                     bg="#17A589", fg="white", font=("Arial", 10, "bold"), cursor="hand2")
        self.btn_guardar.pack(pady=14)
        self.btn_cancelar = tk.Button(self.ventana, text="Volver al inicio", width=22,
                                      command=self.cerrar, cursor="hand2")
        self.btn_cancelar.pack()
        self.entry_nombre.focus_set()

    def obtener_datos(self):
        return (self.entry_nombre.get().strip(), self.entry_email.get().strip(),
                self.entry_password.get(), self.entry_confirmar.get())

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)

    def cerrar(self):
        self.ventana.destroy()
