"""
Ejemplo 02: Crear y Cambiar Entre Escritorios
==============================================

Este ejemplo muestra cómo:
- Crear nuevos escritorios virtuales
- Cambiar entre escritorios
- Eliminar escritorios
- Gestionar múltiples escritorios
"""

import time
from escritorios_virtuales import EscritorioVirtual, GestorEscritorios


def main():
    print("=" * 60)
    print("Ejemplo 02: Crear y Cambiar Entre Escritorios")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    
    # Guardar estado inicial
    escritorios_iniciales = gestor.obtener_escritorios()
    escritorio_inicial = gestor.obtener_escritorio_actual()
    print(f"📊 Estado inicial:")
    print(f"   - Escritorios existentes: {len(escritorios_iniciales)}")
    print(f"   - Escritorio actual: {escritorio_inicial.numero}")
    print()
    
    # Crear un nuevo escritorio
    print("🆕 Creando un nuevo escritorio...")
    nuevo_escritorio = EscritorioVirtual.crear()
    print(f"✓ Escritorio creado: {nuevo_escritorio.nombre} (#{nuevo_escritorio.numero})")
    print()
    
    # Verificar que se creó
    escritorios_actuales = gestor.obtener_escritorios()
    print(f"📊 Escritorios actuales: {len(escritorios_actuales)}")
    print()
    
    # Cambiar al nuevo escritorio
    print(f"🔄 Cambiando al {nuevo_escritorio.nombre}...")
    nuevo_escritorio.ir()
    time.sleep(1)  # Esperar a que se complete la transición
    
    # Verificar que estamos en el nuevo escritorio
    actual = gestor.obtener_escritorio_actual()
    print(f"✓ Escritorio actual: {actual.nombre} (#{actual.numero})")
    print()
    
    # Crear otro escritorio más
    print("🆕 Creando otro escritorio...")
    otro_escritorio = gestor.crear_escritorio()
    print(f"✓ Escritorio creado: {otro_escritorio.nombre} (#{otro_escritorio.numero})")
    print()
    
    # Mostrar todos los escritorios
    print("📋 Lista de todos los escritorios:")
    for escritorio in gestor.obtener_escritorios():
        es_actual = " ← ACTUAL" if escritorio.id == actual.id else ""
        print(f"   - {escritorio.nombre} (#{escritorio.numero}){es_actual}")
    print()
    
    # Navegar entre escritorios
    print("🔄 Navegando entre escritorios...")
    for escritorio in gestor.obtener_escritorios():
        print(f"   Cambiando a {escritorio.nombre}...")
        escritorio.ir()
        time.sleep(0.5)
    print("✓ Navegación completada")
    print()
    
    # Volver al escritorio inicial
    print(f"🏠 Volviendo al escritorio inicial ({escritorio_inicial.numero})...")
    escritorio_inicial.ir()
    time.sleep(0.5)
    print("✓ De vuelta en el escritorio inicial")
    print()
    
    # Limpiar: eliminar los escritorios creados
    print("🧹 Limpiando escritorios creados...")
    
    # Eliminar el segundo escritorio creado
    print(f"   Eliminando {otro_escritorio.nombre}...")
    otro_escritorio.eliminar(respaldo=escritorio_inicial)
    
    # Eliminar el primer escritorio creado
    print(f"   Eliminando {nuevo_escritorio.nombre}...")
    nuevo_escritorio.eliminar(respaldo=escritorio_inicial)
    
    time.sleep(0.5)
    
    # Verificar estado final
    escritorios_finales = gestor.obtener_escritorios()
    print(f"\n📊 Estado final:")
    print(f"   - Escritorios existentes: {len(escritorios_finales)}")
    print(f"   - Escritorio actual: {gestor.obtener_escritorio_actual().numero}")
    
    print("\n✓ Ejemplo completado exitosamente!")
    print("\n💡 Nota: Los escritorios creados fueron eliminados automáticamente.")


def ejemplo_simple():
    """Ejemplo simplificado para referencia rápida"""
    print("\n" + "=" * 60)
    print("Ejemplo Simplificado")
    print("=" * 60)
    print()
    
    # Crear escritorio
    nuevo = EscritorioVirtual.crear()
    print(f"✓ Creado: {nuevo.nombre}")
    
    # Cambiar a él
    nuevo.ir()
    print(f"✓ Cambiado a: {nuevo.nombre}")
    
    # Volver al primero
    escritorios = EscritorioVirtual.obtener_todos()
    escritorios[0].ir()
    print(f"✓ Vuelto a: {escritorios[0].nombre}")
    
    # Eliminar el creado
    nuevo.eliminar()
    print(f"✓ Eliminado: {nuevo.nombre}")


if __name__ == "__main__":
    try:
        main()
        
        # Descomentar para ver el ejemplo simplificado
        # ejemplo_simple()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
