# Instalación Local

Esta guía explica cómo instalar y probar la librería `escritorios-virtuales` localmente antes de publicarla en PyPI.

## Opción 1: Instalación en Modo Desarrollo (Recomendado)

Esta opción permite editar el código y ver los cambios inmediatamente sin reinstalar.

### Pasos:

1. **Navegar al directorio del proyecto:**
   ```bash
   cd escritorios-virtuales
   ```

2. **Instalar en modo editable:**
   ```bash
   pip install -e .
   ```

3. **Verificar la instalación:**
   ```bash
   python prueba_rapida.py
   ```

### Ventajas:
- Los cambios en el código se reflejan inmediatamente
- Ideal para desarrollo y pruebas
- No necesitas reinstalar después de cada cambio

## Opción 2: Instalación Normal

Esta opción instala la librería como un paquete normal.

### Pasos:

1. **Navegar al directorio del proyecto:**
   ```bash
   cd escritorios-virtuales
   ```

2. **Instalar:**
   ```bash
   pip install .
   ```

3. **Verificar la instalación:**
   ```bash
   python -c "from escritorios_virtuales import EscritorioVirtual; print('✓ Instalado correctamente')"
   ```

### Desventajas:
- Necesitas reinstalar después de cada cambio en el código

## Opción 3: Usar sin Instalar

Puedes usar la librería directamente sin instalarla agregando el directorio al PYTHONPATH.

### Pasos:

1. **Navegar al directorio padre:**
   ```bash
   cd ..
   ```

2. **Ejecutar Python con PYTHONPATH:**
   ```bash
   # Windows PowerShell
   $env:PYTHONPATH="escritorios-virtuales"; python
   
   # Windows CMD
   set PYTHONPATH=escritorios-virtuales && python
   ```

3. **Importar y usar:**
   ```python
   from escritorios_virtuales import EscritorioVirtual
   escritorios = EscritorioVirtual.obtener_todos()
   print(f"Escritorios: {len(escritorios)}")
   ```

## Probar la Instalación

### 1. Prueba Rápida

```bash
cd escritorios-virtuales
python prueba_rapida.py
```

Deberías ver:
```
✅ ¡Todas las pruebas pasaron exitosamente!
```

### 2. Ejecutar Ejemplos

```bash
cd ejemplos
python 01_listar_escritorios.py
```

### 3. Prueba en Python Interactivo

```bash
python
```

```python
>>> from escritorios_virtuales import EscritorioVirtual
>>> escritorios = EscritorioVirtual.obtener_todos()
>>> print(f"Tienes {len(escritorios)} escritorios")
>>> actual = EscritorioVirtual.actual()
>>> print(f"Estás en: {actual.nombre}")
```

## Desinstalar

Si instalaste con pip:

```bash
pip uninstall escritorios-virtuales
```

## Problemas Comunes

### Error: "No module named 'escritorios_virtuales'"

**Solución:**
- Verifica que estás en el directorio correcto
- Reinstala: `pip install -e .`
- Verifica la instalación: `pip list | findstr escritorios`

### Error: "COM initialization failed"

**Solución:**
- Asegúrate de estar en Windows 10/11
- Ejecuta Python con permisos normales (no administrador)
- Cierra otras aplicaciones que puedan estar usando COM

### Error al importar ctypes

**Solución:**
- Verifica tu versión de Python: `python --version`
- Debe ser Python 3.7 o superior
- ctypes viene incluido con Python estándar

## Siguiente Paso

Una vez que hayas probado la librería localmente:

1. **Para desarrollo:** Consulta `DESARROLLO.md`
2. **Para publicar:** Consulta la sección de publicación en `DESARROLLO.md`
3. **Para usar:** Consulta `INICIO_RAPIDO.md` y los ejemplos

## Soporte

Si encuentras problemas:

1. Revisa `README.md` para requisitos del sistema
2. Ejecuta `prueba_rapida.py` para diagnóstico
3. Consulta los ejemplos en `ejemplos/`
4. Abre un issue en https://github.com/hxebolax/escritorios-virtuales/issues

## Recursos Adicionales

- `README.md` - Documentación principal
- `INICIO_RAPIDO.md` - Guía de uso rápido
- `DESARROLLO.md` - Guía de desarrollo
- `ejemplos/` - Ejemplos de código
