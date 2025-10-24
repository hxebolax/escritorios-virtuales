"""
Script de Prueba Rápida
========================

Este script realiza una prueba rápida de la librería escritorios-virtuales
para verificar que todo funciona correctamente.
"""

import sys


def prueba_importacion():
    """Probar que se pueden importar los módulos"""
    print("1️⃣  Probando importación de módulos...")
    try:
        from escritorios_virtuales import (
            EscritorioVirtual,
            VistaAplicacion,
            GestorEscritorios
        )
        print("   ✓ Módulos importados correctamente")
        return True
    except ImportError as e:
        print(f"   ❌ Error de importación: {e}")
        return False


def prueba_inicializacion():
    """Probar inicialización del gestor"""
    print("\n2️⃣  Probando inicialización del gestor COM...")
    try:
        from escritorios_virtuales import GestorEscritorios
        gestor = GestorEscritorios()
        print("   ✓ Gestor inicializado correctamente")
        print(f"   ℹ️  Versión de Windows: {gestor.version.nombre_version}")
        return True, gestor
    except Exception as e:
        print(f"   ❌ Error de inicialización: {e}")
        return False, None


def prueba_listar_escritorios(gestor):
    """Probar listado de escritorios"""
    print("\n3️⃣  Probando listado de escritorios...")
    try:
        escritorios = gestor.obtener_escritorios()
        print(f"   ✓ Encontrados {len(escritorios)} escritorios")
        
        for escritorio in escritorios:
            print(f"      - {escritorio.nombre} (#{escritorio.numero})")
        
        return True
    except Exception as e:
        print(f"   ❌ Error al listar escritorios: {e}")
        return False


def prueba_escritorio_actual(gestor):
    """Probar obtención del escritorio actual"""
    print("\n4️⃣  Probando obtención del escritorio actual...")
    try:
        actual = gestor.obtener_escritorio_actual()
        print(f"   ✓ Escritorio actual: {actual.nombre} (#{actual.numero})")
        print(f"   ℹ️  ID: {actual.id}")
        return True
    except Exception as e:
        print(f"   ❌ Error al obtener escritorio actual: {e}")
        return False


def prueba_listar_ventanas(gestor):
    """Probar listado de ventanas"""
    print("\n5️⃣  Probando listado de ventanas...")
    try:
        ventanas = gestor.obtener_ventanas()
        print(f"   ✓ Encontradas {len(ventanas)} ventanas")
        
        if ventanas:
            print("   Primeras 3 ventanas:")
            for ventana in ventanas[:3]:
                anclada = " [ANCLADA]" if ventana.esta_anclada() else ""
                print(f"      - {ventana.titulo[:50]}{anclada}")
        
        return True
    except Exception as e:
        print(f"   ❌ Error al listar ventanas: {e}")
        return False


def prueba_metodos_clase():
    """Probar métodos de clase"""
    print("\n6️⃣  Probando métodos de clase...")
    try:
        from escritorios_virtuales import EscritorioVirtual, VistaAplicacion
        
        # Probar EscritorioVirtual.actual()
        actual = EscritorioVirtual.actual()
        print(f"   ✓ EscritorioVirtual.actual(): {actual.nombre}")
        
        # Probar EscritorioVirtual.obtener_todos()
        todos = EscritorioVirtual.obtener_todos()
        print(f"   ✓ EscritorioVirtual.obtener_todos(): {len(todos)} escritorios")
        
        # Probar VistaAplicacion.actual()
        ventana = VistaAplicacion.actual()
        if ventana:
            print(f"   ✓ VistaAplicacion.actual(): {ventana.titulo[:40]}")
        else:
            print("   ℹ️  VistaAplicacion.actual(): No hay ventana enfocada")
        
        return True
    except Exception as e:
        print(f"   ❌ Error en métodos de clase: {e}")
        return False


def main():
    """Ejecutar todas las pruebas"""
    print("=" * 60)
    print("Prueba Rápida - Escritorios Virtuales")
    print("=" * 60)
    print()
    
    resultados = []
    
    # Prueba 1: Importación
    resultados.append(prueba_importacion())
    
    if not resultados[-1]:
        print("\n❌ No se pudo importar la librería. Verifica la instalación.")
        return False
    
    # Prueba 2: Inicialización
    exito, gestor = prueba_inicializacion()
    resultados.append(exito)
    
    if not exito:
        print("\n❌ No se pudo inicializar el gestor COM.")
        return False
    
    # Prueba 3: Listar escritorios
    resultados.append(prueba_listar_escritorios(gestor))
    
    # Prueba 4: Escritorio actual
    resultados.append(prueba_escritorio_actual(gestor))
    
    # Prueba 5: Listar ventanas
    resultados.append(prueba_listar_ventanas(gestor))
    
    # Prueba 6: Métodos de clase
    resultados.append(prueba_metodos_clase())
    
    # Resumen
    print("\n" + "=" * 60)
    print("Resumen de Pruebas")
    print("=" * 60)
    
    total = len(resultados)
    exitosas = sum(resultados)
    
    print(f"\nPruebas exitosas: {exitosas}/{total}")
    
    if exitosas == total:
        print("\n✅ ¡Todas las pruebas pasaron exitosamente!")
        print("\n💡 La librería está funcionando correctamente.")
        print("   Puedes ejecutar los ejemplos en el directorio 'ejemplos/'")
        return True
    else:
        print(f"\n⚠️  {total - exitosas} prueba(s) fallaron.")
        print("   Revisa los errores anteriores para más detalles.")
        return False


if __name__ == "__main__":
    try:
        exito = main()
        sys.exit(0 if exito else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Prueba interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
