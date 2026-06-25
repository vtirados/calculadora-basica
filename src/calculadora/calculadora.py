from .operaciones import Division, Multiplicacion, Resta, Suma


class Calculadora:
    """Fachada de alto nivel para ejecutar operaciones basicas.

    Esta clase centraliza el acceso a suma, resta, multiplicacion y
    division. Internamente delega el calculo en clases especializadas
    del modulo de operaciones.
    """

    def __init__(self) -> None:
        """Inicializa las dependencias de cada operacion aritmetica."""
        self._suma = Suma()
        self._resta = Resta()
        self._multiplicacion = Multiplicacion()
        self._division = Division()

    def sumar(self, a: float, b: float) -> float:
        """Devuelve la suma de `a` y `b`."""
        return self._suma.ejecutar(a, b)

    def restar(self, a: float, b: float) -> float:
        """Devuelve la resta de `a` menos `b`."""
        return self._resta.ejecutar(a, b)

    def multiplicar(self, a: float, b: float) -> float:
        """Devuelve el producto de `a` por `b`."""
        return self._multiplicacion.ejecutar(a, b)

    def dividir(self, a: float, b: float) -> float:
        """Devuelve la division de `a` entre `b`.

        Puede lanzar `ZeroDivisionError` si `b` es 0.
        """
        return self._division.ejecutar(a, b)
