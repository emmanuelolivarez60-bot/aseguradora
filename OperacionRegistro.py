from datetime import datetime, date


class OperacionRegistro:
    """Utility class for reading validated user input."""

    @staticmethod
    def leer_int(prompt: str, minimo: int = 0, maximo: int | None = None) -> int:
        while True:
            valor = input(prompt)
            if not valor.isdigit():
                print("Error: ingresa un número entero válido.")
                continue

            entero = int(valor)
            if entero < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and entero > maximo:
                print(f"Error: el valor debe ser menor o igual a {maximo}.")
                continue

            return entero

    @staticmethod
    def leer_float(prompt: str, minimo: float = 0.0, maximo: float | None = None) -> float:
        while True:
            valor = input(prompt)
            try:
                numero = float(valor)
            except ValueError:
                print("Error: ingresa un número válido.")
                continue

            if numero < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and numero > maximo:
                print(f"Error: el valor debe ser menor o igual a {maximo}.")
                continue

            return numero

    @staticmethod
    def leer_fecha(prompt: str) -> date:
        while True:
            valor = input(prompt)
            try:
                fecha = datetime.strptime(valor, "%d/%m/%Y").date()
            except ValueError:
                print("Error: ingresa la fecha en el formato DD/MM/YYYY.")
                continue
            return fecha
