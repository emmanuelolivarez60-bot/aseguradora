from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Persona(ABC):
    """
    Clase abstracta que representa los datos generales de una persona.
    """

    nombre: str
    apellidos: str
    fecha_nacimiento: str

    @classmethod
    def capturar_persona(cls):
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
        return nombre, apellidos, fecha_nacimiento

    @abstractmethod
    def obtener_valores(self):
        """
        Método abstracto que obliga a las clases hijas a devolver sus datos.
        """
        pass