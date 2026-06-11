from Cliente import Cliente
from Poliza import Poliza
from Beneficiario import Beneficiario
from Pago import Pago
from Siniestro import Siniestro
from RepositorioBD import RepositorioBD
from GestorEntidadBD import GestorEntidadBD


def mostrar_catalogos():
    repositorio = RepositorioBD("", [])

    while True:
        print("\n===== Catálogos =====")
        print("1. Tipos de póliza")
        print("2. Estatus de póliza")
        print("3. Métodos de pago")
        print("4. Tipos de siniestro")
        print("5. Regresar")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nTipos de póliza:")
            repositorio.consultar_catalogo("catalogo_tipo_poliza")

        elif opcion == "2":
            print("\nEstatus de póliza:")
            repositorio.consultar_catalogo("catalogo_estatus_poliza")

        elif opcion == "3":
            print("\nMétodos de pago:")
            repositorio.consultar_catalogo("catalogo_metodo_pago")

        elif opcion == "4":
            print("\nTipos de siniestro:")
            repositorio.consultar_catalogo("catalogo_tipo_siniestro")

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")


def main():
    """
    Menú principal del sistema VidaFutura.
    """

    repositorios = {
        "1": (
            "Clientes",
            Cliente,
            RepositorioBD("clientes", Cliente.obtener_columnas())
        ),
        "2": (
            "Pólizas",
            Poliza,
            RepositorioBD("polizas", Poliza.obtener_columnas())
        ),
        "3": (
            "Beneficiarios",
            Beneficiario,
            RepositorioBD("beneficiarios", Beneficiario.obtener_columnas())
        ),
        "4": (
            "Pagos",
            Pago,
            RepositorioBD("pagos", Pago.obtener_columnas())
        ),
        "5": (
            "Siniestros",
            Siniestro,
            RepositorioBD("siniestros", Siniestro.obtener_columnas())
        )
    }

    while True:
        print("\n===== Sistema de Seguros VidaFutura =====")
        print("1. Clientes")
        print("2. Pólizas")
        print("3. Beneficiarios")
        print("4. Pagos")
        print("5. Siniestros")
        print("6. Ver catálogos")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "7":
            print("Programa finalizado.")
            break

        elif opcion == "6":
            mostrar_catalogos()

        elif opcion in repositorios:
            nombre, clase, repositorio = repositorios[opcion]

            gestor = GestorEntidadBD(
                nombre,
                clase,
                repositorio
            )

            gestor.mostrar_menu()

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()