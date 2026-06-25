# Calculadora Basica en Python

Proyecto con estructura modular y orientada a clases para operaciones basicas:

- Suma
- Resta
- Multiplicacion
- Division (con manejo de division por cero)

Incluye interfaz interactiva por consola, validacion de entradas numericas y version web con Flask en localhost.

## Estructura

- `src/calculadora/operaciones.py`: clases de operaciones.
- `src/calculadora/calculadora.py`: clase `Calculadora` que orquesta operaciones.
- `src/calculadora/web.py`: app Flask para usar la calculadora en navegador.
- `tests/test_calculadora.py`: pruebas unitarias.
- `tests/test_web.py`: pruebas de la interfaz web.
- `pyproject.toml`: configuracion de empaquetado e instalacion.

## Documentacion de clases

### `Operacion` (clase abstracta)

Ubicacion: `src/calculadora/operaciones.py`

Define el contrato comun `ejecutar(a, b)` para cualquier operacion.
Su objetivo es garantizar una interfaz uniforme entre implementaciones.

### `Suma`

Ubicacion: `src/calculadora/operaciones.py`

Implementa `ejecutar(a, b)` y retorna `a + b`.

### `Resta`

Ubicacion: `src/calculadora/operaciones.py`

Implementa `ejecutar(a, b)` y retorna `a - b`.

### `Multiplicacion`

Ubicacion: `src/calculadora/operaciones.py`

Implementa `ejecutar(a, b)` y retorna `a * b`.

### `Division`

Ubicacion: `src/calculadora/operaciones.py`

Implementa `ejecutar(a, b)` y retorna `a / b`.
Si `b` es 0, lanza `ZeroDivisionError` para proteger la logica de negocio.

### `Calculadora`

Ubicacion: `src/calculadora/calculadora.py`

Actua como fachada: reune las operaciones y expone metodos simples
(`sumar`, `restar`, `multiplicar`, `dividir`) para que la capa web no
dependa de detalles internos.

### `TestCalculadora`

Ubicacion: `tests/test_calculadora.py`

Verifica que la clase `Calculadora` produzca resultados correctos y que
el error por division entre cero se lance cuando corresponde.

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
