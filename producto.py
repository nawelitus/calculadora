class Producto:
    """
    Clase que representa la operación de producto (multiplicación).
    Diseñada para la calculadora bajo el paradigma de Programación Orientada a Objetos (POO).
    """

    def __init__(self, a=None, b=None):
        """
        Constructor de la clase Producto.
        Permite inicializar la instancia con operandos opcionales.
        """
        self.a = a
        self.b = b

    def calcular(self, a=None, b=None):
        """
        Calcula el producto de dos números (a * b).
        
        Permite recibir los valores como argumentos directos (a, b)
        o utilizar los atributos de la instancia (self.a, self.b).
        """
        num1 = a if a is not None else self.a
        num2 = b if b is not None else self.b

        if num1 is None or num2 is None:
            raise ValueError("Se requieren dos valores numéricos para calcular el producto.")

        return num1 * num2

    def __str__(self):
        return "Operación de Producto (Multiplicación)"

    def __repr__(self):
        return f"Producto(a={self.a}, b={self.b})"


# Alias por compatibilidad con main.py si se espera la clase Multiplicacion
Multiplicacion = Producto


if __name__ == "__main__":
    # Pruebas de funcionamiento del módulo
    operacion = Producto()
    print("--- Pruebas de Producto ---")
    print("5 * 4 =", operacion.calcular(5, 4))
    print("-3 * 7 =", operacion.calcular(-3, 7))
    print("2.5 * 2 =", operacion.calcular(2.5, 2))
    print("0 * 10 =", operacion.calcular(0, 10))
