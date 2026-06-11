from dataclasses import dataclass
from datetime import date
from OperacionRegistro import OperacionRegistro


@dataclass
class Poliza:
    """
    Representa una póliza de seguro.
    """

    numero_poliza: int
    fecha_inicio: date
    fecha_fin: date
    prima_mensual: float
    suma_asegurada: float
    tipo_poliza_id: int
    estatus_id: int
    cliente_id: int

    @classmethod
    def capturar(cls):
        numero_poliza = OperacionRegistro.leer_int("Número de póliza: ", minimo=1)

        fecha_inicio = OperacionRegistro.leer_fecha("Fecha inicio (DD/MM/YYYY): ")
        fecha_fin = OperacionRegistro.leer_fecha("Fecha fin (DD/MM/YYYY): ")

        while fecha_inicio >= fecha_fin:
            print("Error: la fecha de inicio debe ser anterior a la fecha de fin")
            fecha_inicio = OperacionRegistro.leer_fecha("Fecha inicio (DD/MM/YYYY): ")
            fecha_fin = OperacionRegistro.leer_fecha("Fecha fin (DD/MM/YYYY): ")

        prima_mensual = OperacionRegistro.leer_float("Prima mensual: ", minimo=1)
        suma_asegurada = OperacionRegistro.leer_float("Suma asegurada: ", minimo=1)

        print("\nTipos de póliza:")
        print("1. Vida")
        print("2. Auto")
        print("3. Gastos médicos")
        print("4. Hogar")
        tipo_poliza_id = OperacionRegistro.leer_int("ID tipo de póliza: ", minimo=1)

        print("\nEstatus de póliza:")
        print("1. Vigente")
        print("2. Vencida")
        print("3. Cancelada")
        estatus_id = OperacionRegistro.leer_int("ID estatus: ", minimo=1)

        cliente_id = OperacionRegistro.leer_int("ID del cliente: ", minimo=1)

        return cls(
            numero_poliza,
            fecha_inicio,
            fecha_fin,
            prima_mensual,
            suma_asegurada,
            tipo_poliza_id,
            estatus_id,
            cliente_id
        )

    def obtener_valores(self):
        return (
            self.numero_poliza,
            self.fecha_inicio,
            self.fecha_fin,
            self.prima_mensual,
            self.suma_asegurada,
            self.tipo_poliza_id,
            self.estatus_id,
            self.cliente_id
        )

    @staticmethod
    def obtener_columnas():
        return [
            "numero_poliza",
            "fecha_inicio",
            "fecha_fin",
            "prima_mensual",
            "suma_asegurada",
            "tipo_poliza_id",
            "estatus_id",
            "cliente_id"
        ]