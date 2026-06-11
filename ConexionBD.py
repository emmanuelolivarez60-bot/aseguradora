import mysql.connector


def obtener_conexion():
    """
    Conecta Python con la base de datos MySQL creada en Laragon.
    """
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema_seguros",
        port=3306
    )
    return conexion