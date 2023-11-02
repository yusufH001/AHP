# Nombre de la app AHP
def adhd(): 
    print("Welcome to ADHD Help Program")
    print("To start press enter ")
    input()

adhd()

listas = {
    "Escuela": ["Hacer tarea de matemáticas", "Estudiar para el examen de historia"],
    "Trabajo": ["Preparar presentación", "Enviar informe"]
    #"Vida"[ ]
}

def mostrar_listas():
    print("Listas Disponibles:")
    for lista in listas:
        print(lista)

def mostrar_tareas(lista):
    print(f"Tareas en la lista '{lista}':")
    for tarea in listas[lista]:
        print(tarea)

def agregar_tarea(lista):
    tarea = input(f"Ingrese una nueva tarea para la lista '{lista}': ")
    listas[lista].append(tarea)
    print(f"'{tarea}' ha sido añadido a la lista '{lista}'.")

while True:
    print("\nOpciones:")
    opciones = ["1. Mostrar Listas", "2. Mostrar Tareas", "3. Añadir Tarea", "4. Salir"]

    for opcion in opciones:
        print(opcion)

    seleccion = input("Seleccione una opción: ")

    if seleccion == "1":
        mostrar_listas()
    elif seleccion == "2":
        lista_seleccionada = input("Ingrese el nombre de la lista: ")
        if lista_seleccionada in listas:
            mostrar_tareas(lista_seleccionada)
        else:
            print("La lista no existe.")
    elif seleccion == "3":
        lista_seleccionada = input("Ingrese el nombre de la lista: ")
        if lista_seleccionada in listas:
            agregar_tarea(lista_seleccionada)
        else:
            print("La lista no existe.")
    elif seleccion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


