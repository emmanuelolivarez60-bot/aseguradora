from dataclasses import dataclass
from Persona import Persona
from OperacionRegistro import OperacionRegistro


@dataclass
class Cliente(Persona):
    """
    Representa a un cliente de la aseguradora.
    Hereda de Persona.
    """

    genero: str
    curp: str
    telefono: str
    correo: str
    ocupacion: str
    ingreso_mensual: float

    @classmethod
    def capturar(cls):
        nombre, apellidos, fecha_nacimiento = Persona.capturar_persona()

        genero = input("Género: ")
        curp = input("CURP: ").upper()

        telefono = input("Teléfono: ")
        while not telefono.isdigit() or len(telefono) != 10:
            print("Error: el teléfono debe tener 10 dígitos numéricos")
            telefono = input("Teléfono: ")

        correo = input("Correo: ")
        ocupacion = input("Ocupación: ")
        ingreso_mensual = OperacionRegistro.leer_float("Ingreso mensual: ", minimo=0)

        return cls(
            nombre,
            apellidos,
            fecha_nacimiento,
            genero,
            curp,
            telefono,
            correo,
            ocupacion,
            ingreso_mensual
        )

    def obtener_valores(self):
        return (
            self.nombre,
            self.apellidos,
            self.fecha_nacimiento,
            self.genero,
            self.curp,
            self.telefono,
            self.correo,
            self.ocupacion,
            self.ingreso_mensual
        )

    @staticmethod
    def obtener_columnas():
        return [
            "nombre",
            "apellidos",
            "fecha_nacimiento",
            "genero",
            "curp",
            "telefono",
            "correo",
            "ocupacion",
            "ingreso_mensual"
        ]