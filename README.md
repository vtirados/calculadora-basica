# Calculadora Basica en Python

Proyecto con estructura modular y enfoque funcional para operaciones basicas:

- Suma
- Resta
- Multiplicacion
- Division (con manejo de division por cero)

Incluye interfaz interactiva por consola, validacion de entradas numericas y version web con Flask en localhost.

## Estructura

- `src/calculadora/calculadora.py`: funcion `calcular(operacion, a, b)`.
- `src/calculadora/web.py`: app Flask para usar la calculadora en navegador.
- `tests/test_calculadora.py`: pruebas unitarias.
- `tests/test_web.py`: pruebas de la interfaz web.
- `pyproject.toml`: configuracion de empaquetado e instalacion.

## Documentacion de funciones

### `calcular`

Ubicacion: `src/calculadora/calculadora.py`

Recibe `operacion`, `a` y `b`, ejecuta `sumar`, `restar`, `multiplicar`
o `dividir`, y retorna el resultado.
Si `b` es 0 al dividir, lanza `ZeroDivisionError("No se puede dividir entre cero")`.
Si la operacion no existe, lanza `ValueError("Operacion no valida")`.

### `TestCalculadora`

Ubicacion: `tests/test_calculadora.py`

Verifica que `calcular(...)` produzca resultados correctos, que se lance
el error por division entre cero y que una operacion invalida lance `ValueError`.

### `TestWebCalculadora`

Ubicacion: `tests/test_web.py`

Valida la aplicacion Flask en tres escenarios: carga de home, calculo de
operacion por formulario y mensaje de error por entrada no numerica.

Proyecto preparado para ejecucion en localhost con Flask.

## Instalar como paquete

```bash
python -m pip install -e .
```

## Ejecutar en localhost con Flask

Instala dependencias:

```bash
python -m pip install -e .
```

Inicia la app web:

```bash
calculadora-web
```

Abre en navegador:

```text
http://127.0.0.1:5000
```

## Probar

```bash
python -m unittest discover -s tests -p "test_*.py"
```
