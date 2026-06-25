from abc import ABC, abstractmethod


class Operacion(ABC):
    """Contrato base para todas las operaciones aritmeticas.

    Cada subclase debe implementar `ejecutar(a, b)` y devolver un numero.
    Este diseno permite separar la logica de cada operacion y facilita
    extender la calculadora con nuevas operaciones sin romper el resto.
    """

    @abstractmethod
    def ejecutar(self, a: float, b: float) -> float:
        """Ejecuta la operacion con dos operandos numericos."""
        raise NotImplementedError


class Suma(Operacion):
    """Implementa la suma de dos numeros."""

    def ejecutar(self, a: float, b: float) -> float:
        """Devuelve `a + b`."""
        return a + b


class Resta(Operacion):
    """Implementa la resta de dos numeros."""

    def ejecutar(self, a: float, b: float) -> float:
        """Devuelve `a - b`."""
        return a - b


class Multiplicacion(Operacion):
    """Implementa la multiplicacion de dos numeros."""

    def ejecutar(self, a: float, b: float) -> float:
        """Devuelve `a * b`."""
        return a * b


class Division(Operacion):
    """Implementa la division de dos numeros.

    Lanza `ZeroDivisionError` cuando el divisor es 0 para evitar
    resultados indefinidos.
    """

    def ejecutar(self, a: float, b: float) -> float:
        """Devuelve `a / b` si `b` es distinto de cero."""
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return a / b
