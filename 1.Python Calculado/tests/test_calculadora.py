import unittest

from src.calculadora.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """Verifica el comportamiento de la clase Calculadora.

    Estas pruebas cubren las cuatro operaciones y el caso de error
    por division entre cero.
    """

    def setUp(self) -> None:
        """Prepara una instancia limpia antes de cada prueba."""
        self.calc = Calculadora()

    def test_suma(self) -> None:
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_resta(self) -> None:
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_multiplicacion(self) -> None:
        self.assertEqual(self.calc.multiplicar(6, 7), 42)

    def test_division(self) -> None:
        self.assertEqual(self.calc.dividir(20, 5), 4)

    def test_division_por_cero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(8, 0)


if __name__ == "__main__":
    unittest.main()
