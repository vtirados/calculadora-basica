from flask import Flask, render_template, request

from .calculadora import calcular


def create_app() -> Flask:
    """Crea y configura la aplicacion Flask de la calculadora.

    Expone dos rutas sobre `/`:
    - GET: muestra el formulario.
    - POST: valida entradas, ejecuta la operacion y muestra resultado.
    """
    app = Flask(__name__, template_folder="templates", static_folder="static")

    @app.get("/")
    def index() -> str:
        return render_template("index.html")

    @app.post("/")
    def calcular_post() -> str:
        numero_a = request.form.get("a", "").strip()
        numero_b = request.form.get("b", "").strip()
        operacion = request.form.get("operacion", "").strip()

        resultado = None
        error = None

        try:
            a = float(numero_a)
            b = float(numero_b)
        except ValueError:
            error = "Debes ingresar valores numericos validos."
            return render_template(
                "index.html",
                numero_a=numero_a,
                numero_b=numero_b,
                operacion=operacion,
                resultado=resultado,
                error=error,
            )

        try:
            resultado = calcular(operacion, a, b)
        except ValueError as exc:
            error = str(exc)
        except ZeroDivisionError as exc:
            error = str(exc)

        return render_template(
            "index.html",
            numero_a=numero_a,
            numero_b=numero_b,
            operacion=operacion,
            resultado=resultado,
            error=error,
        )

    return app


def main() -> None:
    """Punto de entrada para ejecutar la app en localhost."""
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
