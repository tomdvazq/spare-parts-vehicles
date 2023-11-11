import tkinter as tk
from tkinter import ttk, messagebox
from controllers.RepuestoController import RepuestoController
from models.manage_db import borrar_tabla, crear_base_de_datos

# Llamada para borrar la tabla
borrar_tabla()

# Llamada para crear la tabla desde cero
crear_base_de_datos()

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_repuestos = None

        self.campos_repuestos()
        self.deshabilitar_campos()
        self.tabla_repuestos()

    def campos_repuestos(self):
        self.label_denominacion = tk.Label(self, text="Denominación:")
        self.label_denominacion.config(font=("Arial", 12, "bold"))
        self.label_denominacion.grid(row=0, column=0, padx=10, pady=10)

        self.label_codigo = tk.Label(self, text="Código:")
        self.label_codigo.config(font=("Arial", 12, "bold"))
        self.label_codigo.grid(row=1, column=0, padx=10, pady=10)

        self.label_motor = tk.Label(self, text="Motor:")
        self.label_motor.config(font=("Arial", 12, "bold"))
        self.label_motor.grid(row=2, column=0, padx=10, pady=10)

        self.mi_denominacion = tk.StringVar()
        self.entry_denominacion = tk.Entry(self, textvariable=self.mi_denominacion)
        self.entry_denominacion.config(
            width=50,
            font=(
                "Arial",
                12,
            ),
        )
        self.entry_denominacion.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_codigo = tk.StringVar()
        self.entry_codigo = tk.Entry(self, textvariable=self.mi_codigo)
        self.entry_codigo.config(
            width=50,
            font=(
                "Arial",
                12,
            ),
        )
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_motor = tk.StringVar()
        self.entry_motor = tk.Entry(self, textvariable=self.mi_motor)
        self.entry_motor.config(
            width=50,
            font=(
                "Arial",
                12,
            ),
        )
        self.entry_motor.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="green",
            cursor="hand2",
            activebackground="grey",
        )
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="orange",
            cursor="hand2",
            activebackground="grey",
        )
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.deshabilitar_campos
        )
        self.boton_cancelar.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="red",
            cursor="hand2",
            activebackground="grey",
        )
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.mi_denominacion.set("")
        self.mi_codigo.set("")
        self.mi_motor.set("")

        self.entry_denominacion.config(state="normal")
        self.entry_codigo.config(state="normal")
        self.entry_motor.config(state="normal")

        self.boton_guardar.config(state="normal")

    def deshabilitar_campos(self):
        self.id_repuestos = None

        self.mi_denominacion.set("")
        self.mi_codigo.set("")
        self.mi_motor.set("")

        self.entry_denominacion.config(state="disabled")
        self.entry_codigo.config(state="disabled")
        self.entry_motor.config(state="disabled")

        self.boton_guardar.config(state="disabled")

    def tabla_repuestos(self):
        self.lista_repuestos = (
            RepuestoController.listar()
        )  # Cargar la lista de repuestos desde el controlador
        self.tabla = ttk.Treeview(self, column=("Denominación", "Código", "Motor"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky="nse")

        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Denominación")
        self.tabla.heading("#2", text="Código")
        self.tabla.heading("#3", text="Motor")

        for p in self.lista_repuestos:
            self.tabla.insert("", 0, text=p[0], values=(p[1], p[2], p[3]))

        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="green",
            cursor="hand2",
            activebackground="grey",
        )
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_datos
        )
        self.boton_eliminar.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="red",
            cursor="hand2",
            activebackground="grey",
        )
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_repuestos = self.tabla.item(self.tabla.selection())["text"]
            denominacion_repuestos = self.tabla.item(self.tabla.selection())["values"][
                0
            ]
            codigo_repuestos = self.tabla.item(self.tabla.selection())["values"][1]
            motor_repuestos = self.tabla.item(self.tabla.selection())["values"][2]

            self.habilitar_campos()

            self.entry_denominacion.delete(
                0, tk.END
            )  # Limpiar el campo antes de insertar el nuevo valor
            self.entry_denominacion.insert(0, denominacion_repuestos)

            self.entry_codigo.delete(
                0, tk.END
            )  # Limpiar el campo antes de insertar el nuevo valor
            self.entry_codigo.insert(0, codigo_repuestos)

            self.entry_motor.delete(
                0, tk.END
            )  # Limpiar el campo antes de insertar el nuevo valor
            self.entry_motor.insert(0, motor_repuestos)
        except:
            titulo = "Edición de datos"
            mensaje = "No se seleccionó ningún registro"
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_repuestos = self.tabla.item(self.tabla.selection())["text"]
            RepuestoController.eliminar(self.id_repuestos)

            self.tabla_repuestos()
            self.id_repuestos = None

        except:
            titulo = "Eliminar un Registro"
            mensaje = "No se seleccionó ningún registro"
            messagebox.showerror(titulo, mensaje)

    def guardar_datos(self):
        denominacion = self.mi_denominacion.get()
        codigo = self.mi_codigo.get()
        motor = self.mi_motor.get()

        if self.id_repuestos:  # Si id_repuestos tiene un valor, estamos editando
            RepuestoController.editar(self.id_repuestos, denominacion, codigo, motor)
        else:  # De lo contrario, estamos creando un nuevo registro
            RepuestoController.guardar(denominacion, codigo, motor)

        self.tabla_repuestos()
        self.deshabilitar_campos()

def barra_menu(root):
        # Crear una barra de menú
        barra_menu = tk.Menu(root)
        root.config(menu=barra_menu, width=300, height=300)

        # Crear un menú de inicio
        menu_inicio = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

        # Agregar opciones al menú de inicio
        menu_inicio.add_command(
            label="Crear Registro en DB", command=RepuestoController.crear_tabla
        )
        menu_inicio.add_command(
            label="Eliminar Registro en DB", command=RepuestoController.borrar_tabla
        )
        menu_inicio.add_command(label="Salir", command=root.destroy)

        # Agregar otros menús (Consultas, Configuración, Ayuda)
        barra_menu.add_cascade(label="Consultas")
        barra_menu.add_cascade(label="Configuración")
        barra_menu.add_cascade(label="Ayuda")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Repuestos Vehículos")
    barra_menu(root)
    app = Frame(root)
    app.mainloop()
