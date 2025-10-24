"""
Ejemplo 04: Escenarios Prácticos
=================================

Este ejemplo muestra casos de uso del mundo real:
- Organizar ventanas por proyecto
- Limpiar escritorios vacíos
- Crear espacios de trabajo temáticos
- Guardar y restaurar configuraciones
"""

import time
from escritorios_virtuales import EscritorioVirtual, VistaAplicacion, GestorEscritorios


def limpiar_escritorios_vacios():
    """Eliminar escritorios que no tienen ventanas"""
    print("=" * 60)
    print("Limpiar Escritorios Vacíos")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    escritorios = gestor.obtener_escritorios()
    
    print(f"📊 Escritorios totales: {len(escritorios)}\n")
    
    escritorios_vacios = []
    
    for escritorio in escritorios:
        ventanas = escritorio.obtener_ventanas()
        # Filtrar ventanas ancladas para contar solo las específicas del escritorio
        ventanas_especificas = [v for v in ventanas if not v.esta_anclada()]
        
        print(f"🖥️  {escritorio.nombre}:")
        print(f"   Ventanas totales: {len(ventanas)}")
        print(f"   Ventanas específicas: {len(ventanas_especificas)}")
        
        if len(ventanas_especificas) == 0 and len(escritorios) > 1:
            escritorios_vacios.append(escritorio)
            print("   ⚠️  Escritorio vacío (candidato para eliminar)")
        print()
    
    if escritorios_vacios:
        print(f"🧹 Encontrados {len(escritorios_vacios)} escritorios vacíos")
        print("\n⚠️  ADVERTENCIA: Esta operación eliminará escritorios.")
        respuesta = input("¿Deseas continuar? (s/n): ")
        
        if respuesta.lower() == 's':
            escritorio_respaldo = escritorios[0]
            for escritorio in escritorios_vacios:
                if escritorio.id != escritorio_respaldo.id:
                    print(f"   Eliminando {escritorio.nombre}...")
                    try:
                        escritorio.eliminar(respaldo=escritorio_respaldo)
                        print(f"   ✓ Eliminado")
                    except Exception as e:
                        print(f"   ❌ Error: {e}")
            
            print("\n✓ Limpieza completada")
        else:
            print("\n❌ Operación cancelada")
    else:
        print("✓ No hay escritorios vacíos para limpiar")


def crear_espacio_trabajo(nombre_proyecto: str):
    """Crear un nuevo escritorio para un proyecto"""
    print("=" * 60)
    print(f"Crear Espacio de Trabajo: {nombre_proyecto}")
    print("=" * 60)
    print()
    
    # Crear nuevo escritorio
    print(f"🆕 Creando escritorio para '{nombre_proyecto}'...")
    nuevo_escritorio = EscritorioVirtual.crear()
    print(f"✓ Escritorio creado: {nuevo_escritorio.nombre} (#{nuevo_escritorio.numero})")
    
    # Cambiar al nuevo escritorio
    print(f"🔄 Cambiando al nuevo escritorio...")
    nuevo_escritorio.ir()
    time.sleep(1)
    
    print(f"\n✓ Espacio de trabajo listo!")
    print(f"\n💡 Ahora puedes abrir las aplicaciones para '{nombre_proyecto}'")
    print(f"   Todas las ventanas que abras aparecerán en este escritorio.")
    
    return nuevo_escritorio


def mover_ventanas_por_tipo():
    """Organizar ventanas por tipo de aplicación"""
    print("=" * 60)
    print("Organizar Ventanas por Tipo")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    ventanas = gestor.obtener_ventanas()
    
    # Categorizar ventanas
    navegadores = []
    editores = []
    terminales = []
    otras = []
    
    palabras_navegador = ['chrome', 'firefox', 'edge', 'brave', 'opera']
    palabras_editor = ['code', 'visual studio', 'notepad', 'sublime', 'atom']
    palabras_terminal = ['powershell', 'cmd', 'terminal', 'bash']
    
    for ventana in ventanas:
        titulo_lower = ventana.titulo.lower()
        
        if any(palabra in titulo_lower for palabra in palabras_navegador):
            navegadores.append(ventana)
        elif any(palabra in titulo_lower for palabra in palabras_editor):
            editores.append(ventana)
        elif any(palabra in titulo_lower for palabra in palabras_terminal):
            terminales.append(ventana)
        else:
            otras.append(ventana)
    
    print("📊 Ventanas categorizadas:")
    print(f"   🌐 Navegadores: {len(navegadores)}")
    print(f"   📝 Editores: {len(editores)}")
    print(f"   💻 Terminales: {len(terminales)}")
    print(f"   📁 Otras: {len(otras)}")
    print()
    
    if navegadores:
        print("🌐 Navegadores encontrados:")
        for v in navegadores:
            print(f"   - {v.titulo[:50]}")
    
    if editores:
        print("\n📝 Editores encontrados:")
        for v in editores:
            print(f"   - {v.titulo[:50]}")
    
    if terminales:
        print("\n💻 Terminales encontradas:")
        for v in terminales:
            print(f"   - {v.titulo[:50]}")


def resumen_escritorios():
    """Mostrar un resumen completo del estado de los escritorios"""
    print("=" * 60)
    print("Resumen de Escritorios")
    print("=" * 60)
    print()
    
    gestor = GestorEscritorios()
    escritorios = gestor.obtener_escritorios()
    escritorio_actual = gestor.obtener_escritorio_actual()
    
    total_ventanas = 0
    ventanas_ancladas = 0
    
    for escritorio in escritorios:
        es_actual = " ← ACTUAL" if escritorio.id == escritorio_actual.id else ""
        print(f"\n🖥️  {escritorio.nombre}{es_actual}")
        print(f"   ID: {escritorio.id}")
        
        ventanas = escritorio.obtener_ventanas()
        ventanas_especificas = [v for v in ventanas if not v.esta_anclada()]
        ancladas = [v for v in ventanas if v.esta_anclada()]
        
        print(f"   Ventanas específicas: {len(ventanas_especificas)}")
        print(f"   Ventanas ancladas: {len(ancladas)}")
        
        total_ventanas += len(ventanas_especificas)
        ventanas_ancladas = len(ancladas)  # Mismo número en todos
        
        if ventanas_especificas:
            print("   Ventanas:")
            for v in ventanas_especificas[:3]:
                print(f"      • {v.titulo[:45]}")
            if len(ventanas_especificas) > 3:
                print(f"      ... y {len(ventanas_especificas) - 3} más")
    
    print("\n" + "=" * 60)
    print("📊 Estadísticas Globales:")
    print("=" * 60)
    print(f"   Total de escritorios: {len(escritorios)}")
    print(f"   Total de ventanas: {total_ventanas}")
    print(f"   Ventanas ancladas: {ventanas_ancladas}")
    print(f"   Promedio ventanas/escritorio: {total_ventanas / len(escritorios):.1f}")


def ejemplo_flujo_trabajo():
    """Ejemplo de un flujo de trabajo completo"""
    print("=" * 60)
    print("Ejemplo: Flujo de Trabajo Completo")
    print("=" * 60)
    print()
    
    print("Este ejemplo simula un flujo de trabajo típico:")
    print("1. Ver estado actual")
    print("2. Crear escritorio para nuevo proyecto")
    print("3. Organizar ventanas")
    print("4. Limpiar escritorios no usados")
    print()
    
    input("Presiona Enter para comenzar...")
    
    # Paso 1: Estado actual
    print("\n📊 PASO 1: Estado Actual")
    print("-" * 60)
    resumen_escritorios()
    
    input("\nPresiona Enter para continuar...")
    
    # Paso 2: Crear nuevo espacio
    print("\n🆕 PASO 2: Crear Nuevo Espacio de Trabajo")
    print("-" * 60)
    nuevo = crear_espacio_trabajo("Proyecto Python")
    
    input("\nPresiona Enter para continuar...")
    
    # Paso 3: Analizar ventanas
    print("\n📋 PASO 3: Analizar Ventanas")
    print("-" * 60)
    mover_ventanas_por_tipo()
    
    input("\nPresiona Enter para continuar...")
    
    # Paso 4: Limpiar
    print("\n🧹 PASO 4: Limpiar Escritorios Vacíos")
    print("-" * 60)
    limpiar_escritorios_vacios()
    
    print("\n✓ Flujo de trabajo completado!")


def main():
    """Menú principal"""
    print("\n" + "=" * 60)
    print("Ejemplo 04: Escenarios Prácticos")
    print("=" * 60)
    print()
    
    while True:
        print("\nSelecciona una opción:")
        print("1. Resumen de escritorios")
        print("2. Limpiar escritorios vacíos")
        print("3. Crear espacio de trabajo")
        print("4. Organizar ventanas por tipo")
        print("5. Flujo de trabajo completo")
        print("0. Salir")
        print()
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            print()
            resumen_escritorios()
        elif opcion == "2":
            print()
            limpiar_escritorios_vacios()
        elif opcion == "3":
            print()
            nombre = input("Nombre del proyecto: ").strip() or "Nuevo Proyecto"
            crear_espacio_trabajo(nombre)
        elif opcion == "4":
            print()
            mover_ventanas_por_tipo()
        elif opcion == "5":
            print()
            ejemplo_flujo_trabajo()
        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción inválida")
        
        input("\nPresiona Enter para volver al menú...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
