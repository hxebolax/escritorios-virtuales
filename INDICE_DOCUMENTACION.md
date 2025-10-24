# 📚 Índice de Documentación

Guía completa de toda la documentación disponible en el proyecto **escritorios-virtuales**.

## 🚀 Para Empezar

### [EMPEZAR_AQUI.md](EMPEZAR_AQUI.md)
**Inicio rápido en 5 minutos**
- Instalación local
- Primera prueba
- Ejemplos básicos
- Siguiente paso según tu objetivo

### [README.md](README.md)
**Documentación principal del proyecto**
- Descripción general
- Características
- Instalación desde PyPI
- API completa
- Ejemplos de uso
- Limitaciones conocidas

### [INICIO_RAPIDO.md](INICIO_RAPIDO.md)
**Guía de uso rápido**
- Ejemplos de código
- Casos de uso comunes
- Manejo de errores
- Referencia rápida de API

## 💻 Para Desarrolladores

### [INSTALACION_LOCAL.md](INSTALACION_LOCAL.md)
**Instalación y prueba local**
- Instalación en modo desarrollo
- Instalación normal
- Uso sin instalar
- Solución de problemas comunes

### [DESARROLLO.md](DESARROLLO.md)
**Guía completa de desarrollo**
- Configuración del entorno
- Estructura del proyecto
- Testing
- Construcción del paquete
- Publicación en PyPI
- Versionado
- Contribución

### [RESUMEN_PROYECTO.md](RESUMEN_PROYECTO.md)
**Visión general técnica**
- Arquitectura del proyecto
- Componentes técnicos
- Estructura de archivos
- Checklist de publicación

## 💡 Ejemplos

### [ejemplos/README.md](ejemplos/README.md)
**Guía de ejemplos**
- Lista de ejemplos disponibles
- Cómo ejecutarlos
- Requisitos

### Ejemplos de Código

1. **[01_listar_escritorios.py](ejemplos/01_listar_escritorios.py)**
   - Listar todos los escritorios
   - Obtener escritorio actual
   - Mostrar información detallada
   - Listar ventanas por escritorio

2. **[02_crear_y_cambiar.py](ejemplos/02_crear_y_cambiar.py)**
   - Crear nuevos escritorios
   - Cambiar entre escritorios
   - Eliminar escritorios
   - Navegación automática

3. **[03_gestionar_ventanas.py](ejemplos/03_gestionar_ventanas.py)**
   - Listar ventanas
   - Mover ventanas entre escritorios
   - Anclar/desanclar ventanas
   - Enfocar ventanas específicas

4. **[04_escenarios_practicos.py](ejemplos/04_escenarios_practicos.py)**
   - Limpiar escritorios vacíos
   - Crear espacios de trabajo
   - Organizar ventanas por tipo
   - Flujo de trabajo completo

## 🔧 Archivos Técnicos

### [pyproject.toml](pyproject.toml)
**Configuración del paquete**
- Metadatos del proyecto
- Dependencias
- Configuración de build
- Clasificadores de PyPI

### [LICENSE](LICENSE)
**Licencia MIT**
- Términos de uso
- Derechos y limitaciones

### [MANIFEST.in](MANIFEST.in)
**Archivos a incluir en distribución**
- Archivos de código
- Documentación
- Licencia

### [.gitignore](.gitignore)
**Archivos a ignorar en git**
- Archivos compilados
- Directorios de build
- Entornos virtuales
- Archivos del IDE

## 🧪 Herramientas

### [prueba_rapida.py](prueba_rapida.py)
**Script de verificación**
- Prueba de importación
- Prueba de inicialización COM
- Prueba de funcionalidad básica
- Diagnóstico de problemas

## 📖 Guías por Caso de Uso

### Quiero Usar la Librería

1. Lee [EMPEZAR_AQUI.md](EMPEZAR_AQUI.md)
2. Instala: `pip install escritorios-virtuales`
3. Consulta [INICIO_RAPIDO.md](INICIO_RAPIDO.md)
4. Ejecuta ejemplos en `ejemplos/`
5. Lee [README.md](README.md) para API completa

### Quiero Desarrollar/Modificar

1. Lee [EMPEZAR_AQUI.md](EMPEZAR_AQUI.md)
2. Instala localmente: [INSTALACION_LOCAL.md](INSTALACION_LOCAL.md)
3. Configura entorno: [DESARROLLO.md](DESARROLLO.md)
4. Revisa [RESUMEN_PROYECTO.md](RESUMEN_PROYECTO.md)
5. Estudia el código en `escritorios_virtuales/`

### Quiero Publicar en PyPI

1. Lee [DESARROLLO.md](DESARROLLO.md) sección "Publicación"
2. Verifica con `python prueba_rapida.py`
3. Construye: `python -m build`
4. Publica en TestPyPI primero
5. Publica en PyPI

### Quiero Contribuir

1. Lee [DESARROLLO.md](DESARROLLO.md) sección "Contribuir"
2. Fork el repositorio
3. Instala en modo desarrollo
4. Haz tus cambios
5. Ejecuta pruebas
6. Envía Pull Request

## 📂 Estructura de Archivos

```
escritorios-virtuales/
�?
├── 📚 DOCUMENTACIÓN
�?  ├── EMPEZAR_AQUI.md           �?Comienza aquí
�?  ├── README.md                  �?Documentación principal
�?  ├── INICIO_RAPIDO.md          �?Guía de uso rápido
�?  ├── INSTALACION_LOCAL.md      �?Instalación local
�?  ├── DESARROLLO.md             �?Guía de desarrollo
�?  ├── RESUMEN_PROYECTO.md       �?Visión técnica
�?  └── INDICE_DOCUMENTACION.md   �?Este archivo
�?
├── 💻 CÓDIGO FUENTE
�?  └── escritorios_virtuales/
�?      ├── __init__.py           �?API pública
�?      ├── com.py                �?Capa COM
�?      └── nucleo.py             �?Lógica de negocio
�?
├── 💡 EJEMPLOS
�?  └── ejemplos/
�?      ├── README.md
�?      ├── 01_listar_escritorios.py
�?      ├── 02_crear_y_cambiar.py
�?      ├── 03_gestionar_ventanas.py
�?      └── 04_escenarios_practicos.py
�?
├── 🧪 HERRAMIENTAS
�?  └── prueba_rapida.py          �?Script de verificación
�?
└── ⚙️ CONFIGURACIÓN
    ├── pyproject.toml            �?Configuración del paquete
    ├── LICENSE                   �?Licencia MIT
    ├── MANIFEST.in               �?Archivos de distribución
    └── .gitignore                �?Archivos a ignorar
```

## 🔍 Búsqueda Rápida

### ¿Cómo instalo la librería?
�?[EMPEZAR_AQUI.md](EMPEZAR_AQUI.md) o [INSTALACION_LOCAL.md](INSTALACION_LOCAL.md)

### ¿Cómo uso la librería?
�?[INICIO_RAPIDO.md](INICIO_RAPIDO.md) o `ejemplos/`

### ¿Cuál es la API completa?
�?[README.md](README.md) sección "Documentación"

### ¿Cómo desarrollo/modifico?
�?[DESARROLLO.md](DESARROLLO.md)

### ¿Cómo publico en PyPI?
�?[DESARROLLO.md](DESARROLLO.md) sección "Publicación"

### ¿Cómo funciona internamente?
�?[RESUMEN_PROYECTO.md](RESUMEN_PROYECTO.md)

### ¿Hay ejemplos de código?
�?Directorio `ejemplos/`

### ¿Cómo verifico que funciona?
�?`python prueba_rapida.py`

### ¿Qué licencia tiene?
�?[LICENSE](LICENSE) (MIT)

### ¿Cómo contribuyo?
�?[DESARROLLO.md](DESARROLLO.md) sección "Contribuir"

## 📊 Estadísticas del Proyecto

- **Archivos de código:** 3 (com.py, nucleo.py, __init__.py)
- **Ejemplos:** 4 scripts completos
- **Documentación:** 7 archivos .md
- **Líneas de código:** ~1500+
- **Clases principales:** 3 (EscritorioVirtual, VistaAplicacion, GestorEscritorios)
- **Dependencias:** 0 (solo ctypes incluido en Python)

## 🎯 Próximos Pasos Sugeridos

1. **Nuevo usuario:**
   - Lee [EMPEZAR_AQUI.md](EMPEZAR_AQUI.md)
   - Ejecuta `python prueba_rapida.py`
   - Prueba `ejemplos/01_listar_escritorios.py`

2. **Desarrollador:**
   - Lee [DESARROLLO.md](DESARROLLO.md)
   - Instala en modo desarrollo
   - Revisa el código en `escritorios_virtuales/`

3. **Contribuidor:**
   - Lee [DESARROLLO.md](DESARROLLO.md) sección "Contribuir"
   - Fork el repositorio
   - Abre un issue o PR

## 💬 Soporte

Si no encuentras lo que buscas:

1. Revisa este índice de nuevo
2. Busca en [README.md](README.md)
3. Ejecuta `python prueba_rapida.py`
4. Consulta los ejemplos
5. Abre un issue en https://github.com/hxebolax/escritorios-virtuales/issues

---

**Última actualización:** 2025  
**Versión del proyecto:** 1.0.0  
**Autor:** XeBoLaX  
**GitHub:** https://github.com/hxebolax/escritorios-virtuales
