from dataclasses import dataclass
from datetime import date
from OperacionRegistro import OperacionRegistro
from Transaccion import Transaccion


@dataclass
class Pago(Transaccion):
    """
    Representa el pago de una prima.
    Hereda de Transaccion e implementa procesar().
    """

    fecha_pago: date
    monto_pagado: float
    metodo_pago_id: int
    referencia: str
    poliza_id: int

    @classmethod
    def capturar(cls):
        fecha_pago = OperacionRegistro.leer_fecha("Fecha del pago (DD/MM/YYYY): ")
        monto_pagado = OperacionRegistro.leer_float("Monto pagado: ", minimo=1)

        print("\nMétodos de pago:")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Transferencia")
        metodo_pago_id = OperacionRegistro.leer_int("ID método de pago: ", minimo=1)

        referencia = input("Referencia: ")
        poliza_id = OperacionRegistro.leer_int("ID de póliza: ", minimo=1)

        return cls(
            fecha_pago,
            monto_pagado,
            metodo_pago_id,
            referencia,
            poliza_id
        )

    def procesar(self) -> bool:
        if self.monto_pagado <= 0:
            print("Error: el monto pagado debe ser mayor a 0")
            return False

        if self.poliza_id <= 0:
            print("Error: el ID de póliza no es válido")
            return False

        print("Pago procesado correctamente.")
        return True

    def obtener_valores(self):
        return (
            self.fecha_pago,
            self.monto_pagado,
            self.metodo_pago_id,
            self.referencia,
            self.poliza_id
        )

    @staticmethod
    def obtener_columnas():
        return [
            "fecha_pago",
            "monto_pagado",
            "metodo_pago_id",
            "referencia",
            "poliza_id"
        ]