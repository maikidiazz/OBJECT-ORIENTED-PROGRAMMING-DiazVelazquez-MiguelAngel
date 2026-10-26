import mysql.connector
from database.conexion import Conexion


class UserModel:
    def __init__(self):
        self.conexion_db = Conexion()

    def registrar_usuario(self, nombre, email, password):
        conexion = self.conexion_db.conectar()
        if conexion is None:
            return "error"
        cursor = None
        try:
            cursor = conexion.cursor()
            consulta = """INSERT INTO users (nombre, email, password)
                          VALUES (%s, %s, %s)"""
            cursor.execute(consulta, (nombre, email, password))
            conexion.commit()
            return "ok"
        except mysql.connector.IntegrityError:
            conexion.rollback()
            return "duplicado"
        except mysql.connector.Error as error:
            conexion.rollback()
            print("Error al registrar usuario:", error)
            return "error"
        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def validar_usuario(self, email, password):
        conexion = self.conexion_db.conectar()
        if conexion is None:
            return None
        cursor = None
        try:
            cursor = conexion.cursor()
            consulta = """SELECT id, nombre FROM users
                          WHERE email = %s AND password = %s"""
            cursor.execute(consulta, (email, password))
            return cursor.fetchone()
        except mysql.connector.Error as error:
            print("Error al validar usuario:", error)
            return None
        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def cerrar(self):
        # Cada operación abre y cierra su propia conexión.
        pass
