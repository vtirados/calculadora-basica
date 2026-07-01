import unittest

from src.calculadora.calculadora import calcular


class TestCalculadora(unittest.TestCase):
    """Verifica el comportamiento funcional de la calculadora.

    Estas pruebas cubren las cuatro operaciones y el caso de error
    por division entre cero y operacion no soportada.
    """

    def test_suma(self) -> None:
        self.assertEqual(calcular("sumar", 2, 3), 5)

    def test_resta(self) -> None:
        self.assertEqual(calcular("restar", 10, 4), 6)

    def test_multiplicacion(self) -> None:
        self.assertEqual(calcular("multiplicar", 6, 7), 42)

    def test_division(self) -> None:
        self.assertEqual(calcular("dividir", 20, 5), 4)

    def test_division_por_cero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            calcular("dividir", 8, 0)

    def test_operacion_no_valida(self) -> None:
        with self.assertRaisesRegex(ValueError, "Operacion no valida"):
            calcular("modulo", 8, 2)


if __name__ == "__main__":
    unittest.main()
