import tkinter as tk
from tkinter import messagebox

class Cuenta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0

    def registrar_transaccion(self, monto):
        self.balance += monto

class SistemaContable:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, nombre):
        if nombre not in self.cuentas:
            self.cuentas[nombre] = Cuenta(nombre)

    def registrar_transaccion(self, nombre, monto):
        if nombre in self.cuentas:
            self.cuentas[nombre].registrar_transaccion(monto)
        else:
            print(f"La cuenta {nombre} no existe.")

    def generar_balance_general(self):
        balance = "Balance General:\n"
        for nombre, cuenta in self.cuentas.items():
            balance += f"{nombre}: {cuenta.balance}\n"
        return balance

class App:
    def __init__(self, root):
        self.sistema = SistemaContable()
        self.root = root
        self.root.title("Programa Contable")

        self.label_cuenta = tk.Label(root, text="Nombre de la cuenta:")
        self.label_cuenta.pack()
        self.entry_cuenta = tk.Entry(root)
        self.entry_cuenta.pack()

        self.label_monto = tk.Label(root, text="Monto de la transacción:")
        self.label_monto.pack()
        self.entry_monto = tk.Entry(root)
        self.entry_monto.pack()

        self.boton_agregar_cuenta = tk.Button(root, text="Agregar Cuenta", command=self.agregar_cuenta)
        self.boton_agregar_cuenta.pack()

        self.boton_registrar_transaccion = tk.Button(root, text="Registrar Transacción", command=self.registrar_transaccion)
        self.boton_registrar_transaccion.pack()

        self.boton_balance = tk.Button(root, text="Generar Balance General", command=self.mostrar_balance)
        self.boton_balance.pack()

    def agregar_cuenta(self):
        nombre = self.entry_cuenta.get()
        if nombre:
            self.sistema.agregar_cuenta(nombre)
            messagebox.showinfo("Información", f"Cuenta '{nombre}' agregada.")
        else:
            messagebox.showerror("Error", "El nombre de la cuenta no puede estar vacío.")

    def registrar_transaccion(self):
        nombre = self.entry_cuenta.get()
        try:
            monto = float(self.entry_monto.get())
            if nombre in self.sistema.cuentas:
                self.sistema.registrar_transaccion(nombre, monto)
                messagebox.showinfo("Información", f"Transacción de {monto} registrada en '{nombre}'.")
            else:
                messagebox.showerror("Error", f"La cuenta '{nombre}' no existe.")
        except ValueError:
            messagebox.showerror("Error", "Monto inválido. Por favor, ingrese un número.")

    def mostrar_balance(self):
        balance = self.sistema.generar_balance_general()
        messagebox.showinfo("Balance General", balance)

root = tk.Tk()
app = App(root)
root.mainloop()

