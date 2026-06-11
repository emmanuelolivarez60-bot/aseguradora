from dataclasses import dataclass


@dataclass
class PersonaBase:
    """
    Clase base para guardar datos generales de una persona.
    """

    nombre: str
    apellidos: str
    fecha_nacimiento: str

    @classmethod
    def capturar_persona(cls):
        """
        Captura los datos básicos de una persona.
        """
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")

        return nombre, apellidos, fecha_nacimiento