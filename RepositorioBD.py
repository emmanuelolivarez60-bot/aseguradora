import mysql.connector
from ConexionBD import obtener_conexion


class RepositorioBD:
    """
    Clase encargada de realizar operaciones CRUD en MySQL.
    """

    def __init__(self, tabla: str, columnas: list[str]):
        self.tabla = tabla
        self.columnas = columnas

    def registrar(self, valores: tuple) -> bool:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        columnas_texto = ", ".join(self.columnas)
        marcadores = ", ".join(["%s"] * len(self.columnas))

        sql = f"INSERT INTO {self.tabla} ({columnas_texto}) VALUES ({marcadores})"

        try:
            cursor.execute(sql, valores)
            conexion.commit()
            print("Registro guardado correctamente en la base de datos.")
            return True

        except mysql.connector.IntegrityError as error:
            print("Error de integridad en la base de datos.")
            print("Posible causa: CURP duplicada, número de póliza repetido o ID relacionado inexistente.")
            print(f"Detalle técnico: {error}")
            return False

        except mysql.connector.Error as error:
            print("Error al registrar en la base de datos.")
            print(f"Detalle técnico: {error}")
            return False

        finally:
            cursor.close()
            conexion.close()

    def consultar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = f"SELECT * FROM {self.tabla}"
        cursor.execute(sql)

        registros = cursor.fetchall()

        if not registros:
            print("No hay registros.")
        else:
            for registro in registros:
                print(registro)

        cursor.close()
        conexion.close()

    def actualizar(self, id_registro: int, valores: tuple) -> bool:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        asignaciones = ", ".join([f"{columna} = %s" for columna in self.columnas])
        sql = f"UPDATE {self.tabla} SET {asignaciones} WHERE id = %s"

        try:
            cursor.execute(sql, valores + (id_registro,))
            conexion.commit()

            if cursor.rowcount == 0:
                print("No se encontró un registro con ese ID.")
                return False

            print("Registro actualizado correctamente en la base de datos.")
            return True

        except mysql.connector.IntegrityError as error:
            print("Error de integridad en la base de datos.")
            print("Posible causa: dato duplicado o ID relacionado inexistente.")
            print(f"Detalle técnico: {error}")
            return False

        except mysql.connector.Error as error:
            print("Error al actualizar en la base de datos.")
            print(f"Detalle técnico: {error}")
            return False

        finally:
            cursor.close()
            conexion.close()

    def eliminar(self, id_registro: int) -> bool:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = f"DELETE FROM {self.tabla} WHERE id = %s"

        try:
            cursor.execute(sql, (id_registro,))
            conexion.commit()

            if cursor.rowcount == 0:
                print("No se encontró un registro con ese ID.")
                return False

            print("Registro eliminado correctamente de la base de datos.")
            return True

        except mysql.connector.IntegrityError as error:
            print("No se puede eliminar este registro porque está relacionado con otros datos.")
            print(f"Detalle técnico: {error}")
            return False

        finally:
            cursor.close()
            conexion.close()

    def sumar_porcentaje_beneficiarios(self, poliza_id: int) -> float:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT COALESCE(SUM(porcentaje_asignado), 0)
        FROM beneficiarios
        WHERE poliza_id = %s
        """

        cursor.execute(sql, (poliza_id,))
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return float(total)

    def consultar_pagos_por_poliza(self, poliza_id: int):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT pagos.id,
               pagos.fecha_pago,
               pagos.monto_pagado,
               catalogo_metodo_pago.nombre AS metodo_pago,
               pagos.referencia,
               pagos.poliza_id
        FROM pagos
        INNER JOIN catalogo_metodo_pago
            ON pagos.metodo_pago_id = catalogo_metodo_pago.id
        WHERE pagos.poliza_id = %s
        """

        cursor.execute(sql, (poliza_id,))
        registros = cursor.fetchall()

        if not registros:
            print("No hay pagos registrados para esa póliza.")
        else:
            print("\nHistorial de pagos de la póliza:")
            for registro in registros:
                print(registro)

        cursor.close()
        conexion.close()

    def consultar_catalogo(self, tabla_catalogo: str):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = f"SELECT * FROM {tabla_catalogo}"
        cursor.execute(sql)

        registros = cursor.fetchall()

        for registro in registros:
            print(registro)

        cursor.close()
        conexion.close()