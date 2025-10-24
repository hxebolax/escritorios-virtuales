"""
Ejemplo 01: Listar Escritorios Virtuales
=========================================

Este ejemplo muestra cómo:
- Obtener todos los escritorios virtuales
- Obtener el escritorio actual
- Mostrar información sobre cada escritorio
- Listar ventanas en cada escritorio
"""

from escritorios_virtuales import EscritorioVirtual, GestorEscritorios


def main():
    print("=" * 60)
    print("Ejemplo 01: Listar Escritorios Virtuales")
    print("=" * 60)
    print()
    
    # Crear gestor de escritorios
    gestor = GestorEscritorios()
    
    # Obtener todos los escritorios
    print("📋 Obteniendo lista de escritorios...")
    escritorios = gestor.obtener_escritorios()
    print(f"✓ Encontrados {len(escritorios)} escritorios\n")
    
    # Obtener escritorio actual
    escritorio_actual = gestor.obtener_escritorio_actual()
    print(f"📍 Escritorio actual: {escritorio_actual.numero}\n")
    
    # Mostrar información de cada escritorio
    print("=" * 60)
    print("Información de Escritorios:")
    print("=" * 60)
    
    for escritorio in escritorios:
        es_actual = "← ACTUAL" if escritorio.id == escritorio_actual.id else ""
        print(f"\n🖥️  {escritorio.nombre} {es_actual}")
        print(f"   Número: {escritorio.numero}")
        print(f"   ID: {escritorio.id}")
        
        # Obtener ventanas en este escritorio
        ventanas = escritorio.obtener_ventanas()
        print(f"   Ventanas: {len(ventanas)}")
        
        if ventanas:
            print("   Lista de ventanas:")
            for i, ventana in enumerate(ventanas[:5], 1):  # Mostrar máximo 5
                anclada = " [ANCLADA]" if ventana.esta_anclada() else ""
                print(f"      {i}. {ventana.titulo[:50]}{anclada}")
            
            if len(ventanas) > 5:
                print(f"      ... y {len(ventanas) - 5} más")
    
    print("\n" + "=" * 60)
    
    # Método alternativo usando métodos de clase
    print("\n📌 Método alternativo usando métodos de clase:")
    print("-" * 60)
    
    # Obtener escritorio actual directamente
    actual = EscritorioVirtual.actual()
    print(f"Escritorio actual: {actual.nombre} (#{actual.numero})")
    
    # Obtener todos los escritorios directamente
    todos = EscritorioVirtual.obtener_todos()
    print(f"Total de escritorios: {len(todos)}")
    
    print("\n✓ Ejemplo completado exitosamente!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
