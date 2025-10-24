# 🚀 EMPEZAR AQUÍ

¡Bienvenido a **escritorios-virtuales**! Esta guía te ayudará a comenzar en 5 minutos.

## ⚡ Inicio Rápido (5 minutos)

### Paso 1: Instalar Localmente

Abre PowerShell o CMD en este directorio y ejecuta:

```bash
pip install -e .
```

### Paso 2: Verificar Instalación

```bash
python prueba_rapida.py
```

Deberías ver: `✅ ¡Todas las pruebas pasaron exitosamente!`

### Paso 3: Probar un Ejemplo

```bash
cd ejemplos
python 01_listar_escritorios.py
```

¡Listo! Ya tienes la librería funcionando.

## 📖 ¿Qué Puedo Hacer?

### Listar Escritorios

```python
from escritorios_virtuales import EscritorioVirtual

escritorios = EscritorioVirtual.obtener_todos()
for escritorio in escritorios:
    print(f"- {escritorio.nombre}")
```

### Crear Nuevo Escritorio

```python
nuevo = EscritorioVirtual.crear()
nuevo.ir()  # Cambiar a él
```

### Mover Ventana Actual

```python
from escritorios_virtuales import VistaAplicacion

ventana = VistaAplicacion.actual()
escritorios = EscritorioVirtual.obtener_todos()
ventana.mover_a_escritorio(escritorios[0])
```

## 📚 Documentación

- **README.md** - Documentación completa
- **INICIO_RAPIDO.md** - Más ejemplos de código
- **ejemplos/** - 4 ejemplos completos

## 🎯 Ejemplos Disponibles

1. **01_listar_escritorios.py** - Ver escritorios y ventanas
2. **02_crear_y_cambiar.py** - Crear y navegar
3. **03_gestionar_ventanas.py** - Mover y anclar ventanas
4. **04_escenarios_practicos.py** - Casos de uso reales

Ejecuta cualquiera con:
```bash
cd ejemplos
python 01_listar_escritorios.py
```

## 🔧 Desarrollo

Si quieres modificar el código:

1. El código está en `escritorios_virtuales/`
2. Edita los archivos
3. Los cambios se aplican automáticamente (instalación editable)
4. Ejecuta `python prueba_rapida.py` para verificar

Ver **DESARROLLO.md** para más detalles.

## 📦 Publicar en PyPI

Cuando estés listo para publicar:

1. Lee **DESARROLLO.md** sección "Publicación en PyPI"
2. Construye: `python -m build`
3. Publica: `twine upload dist/*`

## ❓ Problemas

### "No module named 'escritorios_virtuales'"

```bash
pip install -e .
```

### "COM initialization failed"

- Asegúrate de estar en Windows 10/11
- No ejecutes como administrador

### Otros problemas

Ejecuta `python prueba_rapida.py` para diagnóstico.

## 🎓 Aprender Más

### Estructura del Código

```
escritorios_virtuales/
├── com.py      # Capa COM (bajo nivel)
├── nucleo.py   # Lógica de negocio (alto nivel)
└── __init__.py # API pública
```

### Clases Principales

- `EscritorioVirtual` - Representa un escritorio
- `VistaAplicacion` - Representa una ventana
- `GestorEscritorios` - Gestor principal

### Flujo Típico

```python
# 1. Importar
from escritorios_virtuales import EscritorioVirtual, VistaAplicacion

# 2. Obtener escritorios
escritorios = EscritorioVirtual.obtener_todos()
actual = EscritorioVirtual.actual()

# 3. Crear nuevo
nuevo = EscritorioVirtual.crear()

# 4. Cambiar
nuevo.ir()

# 5. Gestionar ventanas
ventana = VistaAplicacion.actual()
ventana.mover_a_escritorio(escritorios[0])
```

## 🚀 Siguiente Paso

Elige tu camino:

### 👨‍💻 Quiero Desarrollar
→ Lee **DESARROLLO.md**

### 📚 Quiero Aprender a Usar
→ Lee **INICIO_RAPIDO.md** y ejecuta los ejemplos

### 📦 Quiero Publicar
→ Lee **DESARROLLO.md** sección "Publicación"

### 🤔 Tengo Preguntas
→ Lee **README.md** para documentación completa

## 💡 Tips

1. **Modo desarrollo:** `pip install -e .` permite editar sin reinstalar
2. **Prueba rápida:** `python prueba_rapida.py` verifica todo
3. **Ejemplos:** La mejor forma de aprender es ejecutar los ejemplos
4. **Documentación:** Todos los archivos .md tienen información útil

## 📞 Ayuda

- Revisa **README.md** para documentación completa
- Ejecuta los ejemplos en `ejemplos/`
- Lee **DESARROLLO.md** para desarrollo
- Abre un issue en https://github.com/hxebolax/escritorios-virtuales/issues para bugs

---

**¡Disfruta usando escritorios-virtuales!** 🎉

Si te gusta el proyecto, considera:
- ⭐ Dar una estrella en https://github.com/hxebolax/escritorios-virtuales
- 🐛 Reportar bugs en https://github.com/hxebolax/escritorios-virtuales/issues
- 💡 Sugerir mejoras
- 🤝 Contribuir código
