from OperacionRegistro import OperacionRegistro
from RepositorioBD import RepositorioBD


class GestorEntidadBD:
    """
    Administra el menú CRUD de cada entidad conectada a la base de datos.
    """

    def __init__(self, nombre: str, clase, repositorio: RepositorioBD):
        self.nombre = nombre
        self.clase = clase
        self.repositorio = repositorio

    def mostrar_menu(self):
        while True:
            print(f"\n--- Menú de {self.nombre} ---")
            print("1. Registrar")
            print("2. Consultar")
            print("3. Actualizar")
            print("4. Eliminar")

            if self.nombre == "Beneficiarios":
                print("5. Ver porcentaje total por póliza")
                print("6. Regresar")
            elif self.nombre == "Pagos":
                print("5. Consultar historial de pagos por póliza")
                print("6. Regresar")
            else:
                print("5. Regresar")

            opcion = input("Opción: ")

            if opcion == "1":
                self.registrar()

            elif opcion == "2":
                self.repositorio.consultar()

            elif opcion == "3":
                self.actualizar()

            elif opcion == "4":
                self.eliminar()

            elif opcion == "5" and self.nombre == "Beneficiarios":
                self.ver_porcentaje_total()

            elif opcion == "5" and self.nombre == "Pagos":
                self.consultar_pagos_por_poliza()

            elif opcion == "5":
                break

            elif opcion == "6" and self.nombre in ["Beneficiarios", "Pagos"]:
                break

            else:
                print("Opción no válida.")

    def registrar(self):
        dato = self.clase.capturar()

        if hasattr(dato, "procesar"):
            if not dato.procesar():
                return

        if self.nombre == "Beneficiarios":
            total_actual = self.repositorio.sumar_porcentaje_beneficiarios(dato.poliza_id)
            nuevo_total = total_actual + dato.porcentaje_asignado

            if nuevo_total > 100:
                print("Error: el porcentaje total de beneficiarios no puede superar el 100%.")
                print(f"Porcentaje actual: {total_actual}%")
                print(f"Porcentaje intentado: {dato.porcentaje_asignado}%")
                print(f"Total resultante: {nuevo_total}%")
                return

            self.repositorio.registrar(dato.obtener_valores())

            if nuevo_total == 100:
                print("La póliza ya tiene el 100% asignado en beneficiarios.")
            else:
                print(f"Porcentaje total actual de la póliza: {nuevo_total}%")
                print(f"Falta asignar: {100 - nuevo_total}%")

            return

        self.repositorio.registrar(dato.obtener_valores())

    def actualizar(self):
        id_registro = OperacionRegistro.leer_int(
            "ID del registro a actualizar: ",
            minimo=1
        )

        nuevo_dato = self.clase.capturar()

        if hasattr(nuevo_dato, "procesar"):
            if not nuevo_dato.procesar():
                return

        self.repositorio.actualizar(
            id_registro,
            nuevo_dato.obtener_valores()
        )

    def eliminar(self):
        id_registro = OperacionRegistro.leer_int(
            "ID del registro a eliminar: ",
            minimo=1
        )

        self.repositorio.eliminar(id_registro)

    def ver_porcentaje_total(self):
        poliza_id = OperacionRegistro.leer_int("ID de póliza: ", minimo=1)
        total = self.repositorio.sumar_porcentaje_beneficiarios(poliza_id)

        print(f"Porcentaje total asignado a la póliza {poliza_id}: {total}%")

        if total == 100:
            print("La póliza tiene correctamente asignado el 100%.")
        elif total < 100:
            print(f"Aún falta asignar {100 - total}%.")
        else:
            print("Error: el porcentaje supera el 100%.")

    def consultar_pagos_por_poliza(self):
        poliza_id = OperacionRegistro.leer_int("ID de póliza: ", minimo=1)
        self.repositorio.consultar_pagos_por_poliza(poliza_id)