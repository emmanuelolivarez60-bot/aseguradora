from dataclasses import dataclass
from datetime import date
from OperacionRegistro import OperacionRegistro
from Transaccion import Transaccion


@dataclass
class Siniestro(Transaccion):
    """
    Representa un siniestro o reclamación.
    Hereda de Transaccion e implementa procesar().
    """

    fecha_reporte: date
    fecha_ocurrencia: date
    tipo_siniestro_id: int
    monto_reclamado: float
    monto_aprobado: float
    estatus_siniestro: str
    poliza_id: int

    @classmethod
    def capturar(cls):
        fecha_reporte = OperacionRegistro.leer_fecha("Fecha reporte (DD/MM/YYYY): ")
        fecha_ocurrencia = OperacionRegistro.leer_fecha("Fecha ocurrencia (DD/MM/YYYY): ")

        while fecha_ocurrencia > fecha_reporte:
            print("Error: la fecha de ocurrencia no puede ser posterior a la fecha de reporte")
            fecha_reporte = OperacionRegistro.leer_fecha("Fecha reporte (DD/MM/YYYY): ")
            fecha_ocurrencia = OperacionRegistro.leer_fecha("Fecha ocurrencia (DD/MM/YYYY): ")

        print("\nTipos de siniestro:")
        print("1. Accidente")
        print("2. Robo")
        print("3. Daño")
        print("4. Enfermedad")
        print("5. Fallecimiento")
        tipo_siniestro_id = OperacionRegistro.leer_int("ID tipo de siniestro: ", minimo=1)

        monto_reclamado = OperacionRegistro.leer_float("Monto reclamado: ", minimo=1)
        monto_aprobado = OperacionRegistro.leer_float("Monto aprobado: ", minimo=0)

        while monto_aprobado > monto_reclamado:
            print("Error: el monto aprobado no puede superar al monto reclamado")
            monto_aprobado = OperacionRegistro.leer_float("Monto aprobado: ", minimo=0)

        estatus_siniestro = input("Estatus del siniestro: ")
        poliza_id = OperacionRegistro.leer_int("ID de póliza: ", minimo=1)

        return cls(
            fecha_reporte,
            fecha_ocurrencia,
            tipo_siniestro_id,
            monto_reclamado,
            monto_aprobado,
            estatus_siniestro,
            poliza_id
        )

    def procesar(self) -> bool:
        if self.fecha_ocurrencia > self.fecha_reporte:
            print("Error: la fecha de ocurrencia no puede ser posterior al reporte")
            return False

        if self.monto_reclamado <= 0:
            print("Error: el monto reclamado debe ser mayor a 0")
            return False

        if self.monto_aprobado > self.monto_reclamado:
            print("Error: el monto aprobado supera al reclamado")
            return False

        print("Siniestro procesado correctamente.")
        return True

    def obtener_valores(self):
        return (
            self.fecha_reporte,
            self.fecha_ocurrencia,
            self.tipo_siniestro_id,
            self.monto_reclamado,
            self.monto_aprobado,
            self.estatus_siniestro,
            self.poliza_id
        )

    @staticmethod
    def obtener_columnas():
        return [
            "fecha_reporte",
            "fecha_ocurrencia",
            "tipo_siniestro_id",
            "monto_reclamado",
            "monto_aprobado",
            "estatus_siniestro",
            "poliza_id"
        ]