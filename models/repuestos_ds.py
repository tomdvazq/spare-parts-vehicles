from .conexion_db import ConexionDB
from tkinter import messagebox
from .manage_db import crear_base_de_datos, borrar_tabla

class RepuestoModel:
    @staticmethod
    def crear_tabla():
        crear_base_de_datos()

    @staticmethod
    def borrar_tabla():
        borrar_tabla()

    @staticmethod
    def guardar(denominacion, codigo, motor):
        conexion = ConexionDB()

        sql = f"""INSERT INTO repuestos (denominacion, codigo, motor) VALUES('{denominacion}', '{codigo}', '{motor}' )"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except:
            titulo = 'Conexión al Registro'
            mensaje = 'Tabla no creada en base de datos'
            messagebox.showerror(titulo, mensaje)

    @staticmethod
    def listar():
        conexion = ConexionDB()
        lista_repuestos = []
        sql = "SELECT * FROM repuestos"

        try:
            conexion.cursor.execute(sql)
            lista_repuestos = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            titulo = 'Conexión al Registro'
            mensaje = 'Tabla no creada en base de datos'
            messagebox.showwarning(titulo, mensaje)

        return lista_repuestos

    @staticmethod
    def editar(id_repuestos, denominacion, codigo, motor):
        conexion = ConexionDB()

        sql = f"""UPDATE repuestos SET denominacion = '{denominacion}', codigo = '{codigo}', motor = '{motor}' WHERE id_repuestos = {id_repuestos}"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except:
            titulo = 'Edición de Datos'
            mensaje = 'No se puede editar el registro'
            messagebox.showerror(titulo, mensaje)

    @staticmethod
    def eliminar(id_repuestos):
        conexion = ConexionDB()
        sql = f'DELETE FROM repuestos WHERE id_repuestos = {id_repuestos}'

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except:
            titulo = 'Eliminar Datos'
            mensaje = 'No se puede eliminar el registro'
            messagebox.showerror(titulo, mensaje)
