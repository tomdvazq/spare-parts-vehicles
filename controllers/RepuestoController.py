from models.repuestos_ds import RepuestoModel
from tkinter import messagebox

class RepuestoController:
    @staticmethod
    def guardar(denominacion, codigo, motor):
        try:
            RepuestoModel.guardar(denominacion, codigo, motor)
        except Exception as e:
            messagebox.showerror("Guardar Datos", str(e))

    @staticmethod
    def editar(id_repuestos, denominacion, codigo, motor):
        try:
            RepuestoModel.editar(id_repuestos, denominacion, codigo, motor)
        except Exception as e:
            messagebox.showerror("Editar Datos", str(e))

    @staticmethod
    def eliminar(id_repuestos):
        try:
            RepuestoModel.eliminar(id_repuestos)
        except Exception as e:
            messagebox.showerror("Eliminar Datos", str(e))

    @staticmethod
    def listar():
        try:
            return RepuestoModel.listar()
        except Exception as e:
            messagebox.showwarning("Listar Repuestos", str(e))
            return []
        
    @staticmethod
    def crear_tabla():
        try:
            RepuestoModel.crear_tabla()
            messagebox.showinfo("Crear Tabla", "Tabla creada exitosamente.")
        except Exception as e:
            messagebox.showerror("Crear Tabla", str(e))

    @staticmethod
    def borrar_tabla():
        try:
            RepuestoModel.borrar_tabla()
            messagebox.showinfo("Borrar Tabla", "Tabla borrada exitosamente.")
        except Exception as e:
            messagebox.showerror("Borrar Tabla", str(e))