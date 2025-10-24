# Guía de Desarrollo

Esta guía explica cómo desarrollar, probar y publicar la librería `escritorios-virtuales`.

## Configuración del Entorno de Desarrollo

### 1. Clonar el Repositorio

```bash
git clone https://github.com/hxebolax/escritorios-virtuales.git
cd escritorios-virtuales
```

### 2. Crear Entorno Virtual

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 3. Instalar en Modo Desarrollo

```bash
pip install -e .
```

Esto instala la librería en modo "editable", permitiendo probar cambios sin reinstalar.

## Estructura del Proyecto

```
escritorios-virtuales/
├── escritorios_virtuales/     # Código fuente de la librería
│   ├── __init__.py           # API pública
│   ├── com.py                # Capa COM con ctypes
│   └── nucleo.py             # Lógica de negocio
├── ejemplos/                  # Ejemplos de uso
│   ├── 01_listar_escritorios.py
│   ├── 02_crear_y_cambiar.py
│   ├── 03_gestionar_ventanas.py
│   └── 04_escenarios_practicos.py
├── tests/                     # Tests (opcional)
├── pyproject.toml            # Configuración del paquete
├── README.md                 # Documentación principal
├── LICENSE                   # Licencia MIT
└── DESARROLLO.md             # Esta guía
```

## Desarrollo

### Ejecutar Prueba Rápida

```bash
python prueba_rapida.py
```

Este script verifica que todo funciona correctamente.

### Ejecutar Ejemplos

```bash
cd ejemplos
python 01_listar_escritorios.py
```

### Modificar el Código

1. Edita los archivos en `escritorios_virtuales/`
2. Los cambios se reflejan inmediatamente (instalación editable)
3. Ejecuta `prueba_rapida.py` para verificar

## Testing

### Pruebas Manuales

Ejecuta los ejemplos para probar funcionalidad:

```bash
python ejemplos/01_listar_escritorios.py
python ejemplos/02_crear_y_cambiar.py
python ejemplos/03_gestionar_ventanas.py
python ejemplos/04_escenarios_practicos.py
```

### Pruebas Automatizadas (Opcional)

Si deseas agregar tests automatizados:

```bash
pip install pytest
pytest tests/
```

## Construcción del Paquete

### 1. Instalar Herramientas de Build

```bash
pip install build twine
```

### 2. Limpiar Builds Anteriores

```bash
rmdir /s /q build dist *.egg-info  # Windows
```

### 3. Construir el Paquete

```bash
python -m build
```

Esto crea:
- `dist/escritorios-virtuales-1.0.0.tar.gz` (código fuente)
- `dist/escritorios_virtuales-1.0.0-py3-none-any.whl` (wheel)

### 4. Verificar el Paquete

```bash
twine check dist/*
```

## Publicación en PyPI

### Publicación en TestPyPI (Recomendado Primero)

1. Crear cuenta en https://test.pypi.org/

2. Subir a TestPyPI:

```bash
twine upload --repository testpypi dist/*
```

3. Probar instalación desde TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ escritorios-virtuales
```

### Publicación en PyPI (Producción)

1. Crear cuenta en https://pypi.org/

2. Subir a PyPI:

```bash
twine upload dist/*
```

3. Instalar desde PyPI:

```bash
pip install escritorios-virtuales
```

## Versionado

Sigue [Semantic Versioning](https://semver.org/):

- `1.0.0` - Versión inicial
- `1.0.1` - Corrección de bugs
- `1.1.0` - Nueva funcionalidad (compatible)
- `2.0.0` - Cambios incompatibles

Para actualizar la versión:

1. Edita `pyproject.toml`:
   ```toml
   version = "1.0.1"
   ```

2. Crea un tag en git:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

## Checklist de Publicación

Antes de publicar una nueva versión:

- [ ] Actualizar número de versión en `pyproject.toml`
- [ ] Actualizar `README.md` si hay cambios en la API
- [ ] Ejecutar `prueba_rapida.py` exitosamente
- [ ] Probar todos los ejemplos
- [ ] Limpiar builds anteriores
- [ ] Construir nuevo paquete
- [ ] Verificar con `twine check`
- [ ] Probar en TestPyPI primero
- [ ] Publicar en PyPI
- [ ] Crear tag en git
- [ ] Actualizar documentación

## Contribuir

### Reportar Bugs

Abre un issue en GitHub con:
- Descripción del problema
- Pasos para reproducir
- Versión de Windows
- Versión de Python
- Código de ejemplo

### Proponer Mejoras

Abre un issue describiendo:
- La funcionalidad propuesta
- Casos de uso
- Ejemplo de API deseada

### Enviar Pull Requests

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Haz tus cambios
4. Ejecuta pruebas
5. Commit: `git commit -am 'Añadir nueva funcionalidad'`
6. Push: `git push origin feature/nueva-funcionalidad`
7. Abre un Pull Request

## Recursos

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)
- [Python ctypes](https://docs.python.org/3/library/ctypes.html)

## Soporte

- GitHub Issues: https://github.com/hxebolax/escritorios-virtuales/issues
- GitHub: https://github.com/hxebolax/escritorios-virtuales

## Licencia

MIT License - ver archivo LICENSE para más detalles
