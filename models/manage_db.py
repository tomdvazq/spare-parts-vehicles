from .conexion_db import ConexionDB
from tkinter import messagebox

def borrar_tabla():
    conexion = ConexionDB()
    # Eliminar la tabla si ya existe
    try:
        conexion.cursor.execute("DROP TABLE repuestos")
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Tabla eliminada en base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        pass  # Si la tabla no existe, no hay necesidad de mostrar un mensaje

def crear_base_de_datos():
    conexion = ConexionDB()

    # Crear la tabla nuevamente
    sql = """CREATE TABLE repuestos (
                id_repuestos INTEGER PRIMARY KEY AUTOINCREMENT,
                denominacion VARCHAR(100),
                codigo VARCHAR(10),
                motor VARCHAR(100)
            )"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Tabla añadida en base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'Error al crear la tabla'
        messagebox.showerror(titulo, mensaje)
