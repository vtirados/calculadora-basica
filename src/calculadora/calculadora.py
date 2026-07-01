def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


OPERACIONES = {
    "sumar": lambda a, b: a + b,
    "restar": lambda a, b: a - b,
    "multiplicar": lambda a, b: a * b,
    "dividir": dividir,
}


def calcular(operacion: str, a: float, b: float) -> float:
    try:
        return OPERACIONES[operacion](a, b)
    except KeyError as exc:
        raise ValueError("Operacion no valida") from exc
