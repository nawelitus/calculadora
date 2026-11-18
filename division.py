class Division:
    """Clase para la operación de división en la calculadora."""

    def calcular(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b


def division(a, b):
    """Función de división entre dos números."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
