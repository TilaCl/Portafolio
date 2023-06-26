
import os

PROPOSITO = '''
Gestor de tareas: Crea una aplicación que permita
agregar, editar y eliminar tareas 
con fechas de vencimiento y prioridades.
'''


LISTA = [" "]

TEXTO = '''
Gestor de tareas 
1. Nueva tarea
2. Editar tarea
3. Eliminar tarea
4. ELIMINAR TODO
5. Salir
'''

while True:
    os.system('cls')
    print(TEXTO)
    for i, tarea in enumerate(LISTA, start=1):
        print(f"{i}. {tarea}")

    opcion = int(input("Elige una opción: "))

    if opcion == 1: # Agregar tarea
        os.system('cls')
        tarea = input("Ingresa una tarea: ")
        LISTA.append(tarea)
        print(f"Tarea agregada: {tarea}")

    elif opcion == 2:  # Editar tarea
        os.system('cls')
        for i, tarea in enumerate(LISTA, start=1):
            print(f"{i}. {tarea}")
        N_LISTA = int(input("¿Qué tarea deseas modificar?: "))
        if 1 <= N_LISTA <= len(LISTA):
            nueva_tarea = input("Ingresa la nueva tarea: ")
            LISTA[N_LISTA-1] = nueva_tarea
            print(f"Tarea modificada: {nueva_tarea}")
        else:
            print("¡Opción no válida!")

    elif opcion == 3:  # Eliminar tarea
        os.system('cls')
        for i, tarea in enumerate(LISTA, start=1):
            print(f"{i}. {tarea}")
        N_LISTA = int(input("¿Qué tarea deseas ELIMINAR?: "))
        if 1 <= N_LISTA <= len(LISTA):
            tarea_eliminada = LISTA.pop(N_LISTA-1)
            print(f"Tarea eliminada: {tarea_eliminada}")
        else:
            print("¡Opción no válida!")

    elif opcion == 4:  # Eliminar todas las tareas
        LISTA.clear()
        print("Todas las tareas han sido eliminadas.")

    elif opcion == 5:
        print("¡Adiós!")
        break

    else:
        print("¡Opción no válida!")

    input("Presiona Enter para continuar...")