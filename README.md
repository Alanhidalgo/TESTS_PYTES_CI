# TESTS_PYTEST_CI

## Descripción

`TESTS_PYTEST_CI` es un proyecto de pruebas automatizadas utilizando Selenium WebDriver y pytest. Este proyecto está configurado para ejecutarse en GitHub Actions para integración continua.

## Instalación

Para instalar las dependencias necesarias, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/TESTS_PYTEST_CI.git
    ```

2. Navega a la carpeta del proyecto:
    ```bash
    cd TESTS_PYTEST_CI
    ```

3. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:
    - En **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - En **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar las pruebas, usa el siguiente comando:

```bash
pytest --browser=chrome


## Contribuciones
Si deseas contribuir al proyecto, por favor sigue estos pasos:

Fork el repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Crea una nueva pull request.