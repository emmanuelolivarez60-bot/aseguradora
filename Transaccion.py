from abc import ABC, abstractmethod


class Transaccion(ABC):
    """
    Clase abstracta para operaciones que deben procesarse.
    """

    @abstractmethod
    def procesar(self) -> bool:
        """
        Método obligatorio para las clases que hereden de Transaccion.
        """
        pass