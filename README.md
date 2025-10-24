# Escritorios Virtuales

Una librería Python ligera y sin dependencias para gestionar escritorios virtuales de Windows 10/11.

## 🌟 Características

- ✅ **Sin dependencias externas** - Solo usa ctypes puro (sin comtypes, sin pywin32)
- ✅ **API en español** - Nombres de clases y métodos completamente en español
- ✅ **Soporte completo** - Windows 10 (build 10240+) y Windows 11
- ✅ **Funcionalidad completa**:
  - Listar, crear y eliminar escritorios virtuales
  - Cambiar entre escritorios
  - Mover ventanas entre escritorios
  - Anclar/desanclar ventanas (mostrar en todos los escritorios)
  - Obtener información de ventanas y escritorios

## 📦 Instalación

```bash
pip install escritorios-virtuales
```

## 🚀 Inicio Rápido

```python
from escritorios_virtuales import EscritorioVirtual, VistaAplicacion

# Listar todos los escritorios
escritorios = EscritorioVirtual.obtener_todos()
print(f"Tienes {len(escritorios)} escritorios")

# Obtener escritorio actual
actual = EscritorioVirtual.actual()
print(f"Estás en el escritorio {actual.numero}")

# Crear un nuevo escritorio
nuevo = EscritorioVirtual.crear()
print(f"Creado escritorio {nuevo.numero}")

# Cambiar a un escritorio
escritorios[0].ir()

# Obtener ventana actual
ventana = VistaAplicacion.actual()
if ventana:
    print(f"Ventana actual: {ventana.titulo}")
    
    # Mover ventana a otro escritorio
    ventana.mover_a_escritorio(escritorios[1])
    
    # Anclar ventana (mostrar en todos los escritorios)
    ventana.anclar()
```

## 📚 Ejemplos

Consulta el directorio `ejemplos/` para ver casos de uso completos:

- `01_listar_escritorios.py` - Listar y obtener información de escritorios
- `02_crear_y_cambiar.py` - Crear escritorios y cambiar entre ellos
- `03_gestionar_ventanas.py` - Mover y anclar ventanas
- `04_escenarios_practicos.py` - Casos de uso del mundo real

## 🔧 Requisitos

- Windows 10 (build 10240 o superior) o Windows 11
- Python 3.7 o superior
- Sin dependencias adicionales

## 📖 Documentación

### Clase `EscritorioVirtual`

Representa un escritorio virtual de Windows.

**Propiedades:**
- `id` - GUID único del escritorio
- `numero` - Número del escritorio (1-based)
- `nombre` - Nombre del escritorio

**Métodos:**
- `ir()` - Cambiar a este escritorio
- `eliminar(respaldo=None)` - Eliminar este escritorio
- `obtener_ventanas()` - Obtener ventanas en este escritorio

**Métodos estáticos:**
- `actual()` - Obtener el escritorio actual
- `crear()` - Crear un nuevo escritorio
- `obtener_todos()` - Obtener lista de todos los escritorios

### Clase `VistaAplicacion`

Representa una ventana de aplicación.

**Propiedades:**
- `hwnd` - Handle de la ventana
- `titulo` - Título de la ventana
- `id_aplicacion` - ID de la aplicación
- `escritorio` - Escritorio donde está la ventana

**Métodos:**
- `mover_a_escritorio(escritorio)` - Mover a otro escritorio
- `anclar()` - Anclar ventana (mostrar en todos los escritorios)
- `desanclar()` - Desanclar ventana
- `esta_anclada()` - Verificar si está anclada
- `enfocar()` - Enfocar esta ventana

**Métodos estáticos:**
- `actual()` - Obtener la ventana actualmente enfocada

## ⚠️ Limitaciones Conocidas

- Solo funciona en Windows 10/11
- Requiere permisos de usuario normales (no necesita administrador)
- Algunas operaciones pueden fallar si Windows está en transición entre escritorios

## 🤝 Contribuir

Las contribuciones son bienvenidas! Por favor:

1. Haz fork del repositorio en https://github.com/hxebolax/escritorios-virtuales
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

MIT License - ver archivo LICENSE para más detalles

## 🙏 Agradecimientos

Esta librería está inspirada en el trabajo de la comunidad de desarrolladores que han explorado las APIs internas de Windows para escritorios virtuales.

## 📞 Soporte

Si encuentras algún problema o tienes preguntas:
- Abre un issue en https://github.com/hxebolax/escritorios-virtuales/issues
- Consulta los ejemplos en el directorio `ejemplos/`
- Revisa la documentación en el README
