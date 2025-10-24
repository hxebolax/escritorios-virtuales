"""
Ejemplo 03: Gestionar Ventanas
===============================

Este ejemplo muestra cómo:
- Obtener información de ventanas
- Mover ventanas entre escritorios
- Anclar y desanclar ventanas
- Enfocar ventanas específicas
"""

import time
from escritorios_virtuales import EscritorioVirtual, VistaAplicacion, GestorEscritorios


def listar_ventanas():
    """Listar todas las ventanas y su información"""
    print("=" * 60)
    print("Listar Ventanas")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    
    # Obtener todas las ventanas
    ventanas = gestor.obtener_ventanas()
    print(f"📋 Total de ventanas: {len(ventanas)}\n")
    
    # Mostrar información de cada ventana
    for i, ventana in enumerate(ventanas, 1):
        print(f"{i}. {ventana.titulo}")
        print(f"   HWND: {ventana.hwnd}")
        print(f"   Escritorio: {ventana.escritorio.numero}")
        print(f"   Anclada: {'Sí' if ventana.esta_anclada() else 'No'}")
        if ventana.id_aplicacion:
            print(f"   App ID: {ventana.id_aplicacion}")
        print()


def mover_ventana_actual():
    """Mover la ventana actual a otro escritorio"""
    print("=" * 60)
    print("Mover Ventana Actual")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    
    # Obtener ventana actual
    ventana_actual = gestor.obtener_ventana_actual()
    
    if not ventana_actual:
        print("❌ No hay ventana enfocada actualmente")
        return
    
    print(f"🪟 Ventana actual: {ventana_actual.titulo}")
    print(f"   Escritorio actual: {ventana_actual.escritorio.numero}")
    print()
    
    # Obtener escritorios
    escritorios = gestor.obtener_escritorios()
    
    if len(escritorios) < 2:
        print("⚠️  Necesitas al menos 2 escritorios para mover ventanas")
        print("   Creando un escritorio adicional...")
        nuevo = EscritorioVirtual.crear()
        escritorios = gestor.obtener_escritorios()
        print(f"✓ Escritorio creado: {nuevo.nombre}")
        print()
    
    # Encontrar un escritorio diferente
    escritorio_destino = None
    for escritorio in escritorios:
        if escritorio.id != ventana_actual.escritorio.id:
            escritorio_destino = escritorio
            break
    
    if escritorio_destino:
        print(f"🔄 Moviendo ventana al {escritorio_destino.nombre}...")
        ventana_actual.mover_a_escritorio(escritorio_destino)
        time.sleep(0.5)
        print(f"✓ Ventana movida exitosamente")
        print()
        
        # Verificar
        print("🔍 Verificando...")
        # Refrescar la información de la ventana
        ventanas = gestor.obtener_ventanas()
        for v in ventanas:
            if v.hwnd == ventana_actual.hwnd:
                print(f"   Escritorio actual de la ventana: {v.escritorio.numero}")
                break


def anclar_ventana_actual():
    """Anclar/desanclar la ventana actual"""
    print("=" * 60)
    print("Anclar/Desanclar Ventana")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    
    # Obtener ventana actual
    ventana_actual = gestor.obtener_ventana_actual()
    
    if not ventana_actual:
        print("❌ No hay ventana enfocada actualmente")
        return
    
    print(f"🪟 Ventana: {ventana_actual.titulo}")
    esta_anclada = ventana_actual.esta_anclada()
    print(f"   Estado actual: {'Anclada' if esta_anclada else 'No anclada'}")
    print()
    
    if esta_anclada:
        print("📌 Desanclando ventana...")
        ventana_actual.desanclar()
        print("✓ Ventana desanclada (ahora solo aparece en un escritorio)")
    else:
        print("📌 Anclando ventana...")
        ventana_actual.anclar()
        print("✓ Ventana anclada (ahora aparece en todos los escritorios)")
    
    print()
    print("💡 Tip: Las ventanas ancladas aparecen en todos los escritorios")


def organizar_ventanas_por_escritorio():
    """Ejemplo de organización de ventanas"""
    print("=" * 60)
    print("Organizar Ventanas por Escritorio")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    escritorios = gestor.obtener_escritorios()
    
    print("📊 Distribución actual de ventanas:\n")
    
    for escritorio in escritorios:
        ventanas = escritorio.obtener_ventanas()
        print(f"🖥️  {escritorio.nombre}:")
        print(f"   Ventanas: {len(ventanas)}")
        
        if ventanas:
            for ventana in ventanas[:3]:  # Mostrar primeras 3
                anclada = " [ANCLADA]" if ventana.esta_anclada() else ""
                print(f"      - {ventana.titulo[:40]}{anclada}")
            
            if len(ventanas) > 3:
                print(f"      ... y {len(ventanas) - 3} más")
        print()


def ejemplo_enfocar_ventana():
    """Ejemplo de cómo enfocar una ventana específica"""
    print("=" * 60)
    print("Enfocar Ventana")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    ventanas = gestor.obtener_ventanas()
    
    if not ventanas:
        print("❌ No hay ventanas disponibles")
        return
    
    print("📋 Ventanas disponibles:")
    for i, ventana in enumerate(ventanas[:5], 1):
        print(f"   {i}. {ventana.titulo[:50]}")
    print()
    
    # Enfocar la primera ventana como ejemplo
    if ventanas:
        ventana = ventanas[0]
        print(f"🎯 Enfocando: {ventana.titulo}")
        print(f"   (Escritorio: {ventana.escritorio.numero})")
        
        try:
            ventana.enfocar()
            print("✓ Ventana enfocada exitosamente")
        except Exception as e:
            print(f"⚠️  No se pudo enfocar: {e}")


def main():
    """Menú principal de ejemplos"""
    print("\n" + "=" * 60)
    print("Ejemplo 03: Gestionar Ventanas")
    print("=" * 60)
    print()
    print("Este ejemplo muestra diferentes operaciones con ventanas.")
    print("Ejecuta cada función individualmente para ver los resultados.")
    print()
    
    # Ejecutar ejemplos
    print("\n1️⃣  LISTAR VENTANAS")
    print("-" * 60)
    listar_ventanas()
    
    input("\nPresiona Enter para continuar...")
    
    print("\n2️⃣  ORGANIZAR VENTANAS")
    print("-" * 60)
    organizar_ventanas_por_escritorio()
    
    input("\nPresiona Enter para continuar...")
    
    print("\n3️⃣  ENFOCAR VENTANA")
    print("-" * 60)
    ejemplo_enfocar_ventana()
    
    print("\n" + "=" * 60)
    print("✓ Ejemplos completados!")
    print()
    print("💡 Para probar mover o anclar ventanas, descomenta las")
    print("   funciones correspondientes en el código.")


if __name__ == "__main__":
    try:
        main()
        
        # Descomentar para probar estas funciones:
        # print("\n")
        # mover_ventana_actual()
        # print("\n")
        # anclar_ventana_actual()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
