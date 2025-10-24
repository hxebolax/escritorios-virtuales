# Inicio Rápido - Escritorios Virtuales

## Instalación

```bash
pip install escritorios-virtuales
```

## Uso Básico

### 1. Listar Escritorios

```python
from escritorios_virtuales import EscritorioVirtual

# Obtener todos los escritorios
escritorios = EscritorioVirtual.obtener_todos()
print(f"Tienes {len(escritorios)} escritorios")

# Mostrar información
for escritorio in escritorios:
    print(f"- {escritorio.nombre} (#{escritorio.numero})")
```

### 2. Obtener Escritorio Actual

```python
from escritorios_virtuales import EscritorioVirtual

actual = EscritorioVirtual.actual()
print(f"Estás en: {actual.nombre}")
```

### 3. Crear Nuevo Escritorio

```python
from escritorios_virtuales import EscritorioVirtual

# Crear escritorio
nuevo = EscritorioVirtual.crear()
print(f"Creado: {nuevo.nombre}")

# Cambiar a él
nuevo.ir()
```

### 4. Trabajar con Ventanas

```python
from escritorios_virtuales import VistaAplicacion, EscritorioVirtual

# Obtener ventana actual
ventana = VistaAplicacion.actual()
if ventana:
    print(f"Ventana: {ventana.titulo}")
    
    # Mover a otro escritorio
    escritorios = EscritorioVirtual.obtener_todos()
    ventana.mover_a_escritorio(escritorios[0])
    
    # Anclar (mostrar en todos los escritorios)
    ventana.anclar()
```

### 5. Gestión Completa

```python
from escritorios_virtuales import GestorEscritorios

gestor = GestorEscritorios()

# Obtener escritorios
escritorios = gestor.obtener_escritorios()
actual = gestor.obtener_escritorio_actual()

# Crear nuevo
nuevo = gestor.crear_escritorio()

# Obtener ventanas
ventanas = gestor.obtener_ventanas()
ventana_actual = gestor.obtener_ventana_actual()

# Obtener ventanas de un escritorio específico
ventanas_escritorio = gestor.obtener_ventanas(escritorio=actual)
```

## Ejemplos Completos

Consulta el directorio `ejemplos/` para ver casos de uso completos:

- `01_listar_escritorios.py` - Listar y obtener información
- `02_crear_y_cambiar.py` - Crear y navegar entre escritorios
- `03_gestionar_ventanas.py` - Mover y anclar ventanas
- `04_escenarios_practicos.py` - Casos de uso del mundo real

## Ejecutar Ejemplos

```bash
cd ejemplos
python 01_listar_escritorios.py
```

## Manejo de Errores

```python
from escritorios_virtuales import (
    EscritorioVirtual,
    ExcepcionEVD,
    OperacionNoSoportada
)

try:
    escritorio = EscritorioVirtual.crear()
    escritorio.ir()
except OperacionNoSoportada as e:
    print(f"Operación no soportada: {e}")
except ExcepcionEVD as e:
    print(f"Error: {e}")
```

## Requisitos

- Windows 10 (build 10240+) o Windows 11
- Python 3.7 o superior
- Sin dependencias adicionales

## Soporte

- GitHub: https://github.com/hxebolax/escritorios-virtuales
- Issues: https://github.com/hxebolax/escritorios-virtuales/issues
- Documentación: Ver README.md

## Licencia

MIT License - ver archivo LICENSE para más detalles
