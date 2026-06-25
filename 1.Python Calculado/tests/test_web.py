import unittest

from src.calculadora.web import create_app


class TestWebCalculadora(unittest.TestCase):
    """Valida la integracion HTTP basica de la calculadora web.

    Comprueba renderizado de la pagina principal, calculo por formulario
    y mensajes de validacion cuando la entrada es invalida.
    """

    def setUp(self) -> None:
        """Crea un cliente de pruebas Flask para peticiones simuladas."""
        app = create_app()
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_disponible(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Calculadora en Localhost", response.get_data(as_text=True))

    def test_suma_desde_formulario(self) -> None:
        response = self.client.post(
            "/",
            data={"a": "2", "b": "3", "operacion": "sumar"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Resultado", response.get_data(as_text=True))
        self.assertIn("5.0", response.get_data(as_text=True))

    def test_error_entrada_no_numerica(self) -> None:
        response = self.client.post(
            "/",
            data={"a": "abc", "b": "2", "operacion": "sumar"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Debes ingresar valores numericos validos.",
            response.get_data(as_text=True),
        )


if __name__ == "__main__":
    unittest.main()
