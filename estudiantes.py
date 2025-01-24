# Lista para almacenar los estudiantes
estudiantes = []

# Función para agregar un estudiante
def agregar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    grado = input("Ingrese el grado del estudiante: ")

    estudiante = {"nombre": nombre, "edad": edad, "grado": grado}
    estudiantes.append(estudiante)
    print(f"\nEl estudiante '{nombre}' ha sido agregado con éxito.")

# Función para eliminar un estudiante
def eliminar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante que desea eliminar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiantes.remove(estudiante)
            print(f"\nEl estudiante '{nombre}' ha sido eliminado.")
            return
    print(f"\nEl estudiante '{nombre}' no se encontró.")

# Función para buscar un estudiante
def buscar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante que desea buscar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"\nEstudiante encontrado: Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")
            return
    print(f"\nEl estudiante '{nombre}' no se encontró.")

# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    if estudiantes:
        print("\nLista de estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")
    else:
        print("\nNo hay estudiantes registrados.")

# Menú principal
def menu_estudiantes():
    while True:
        print("\n--- Sistema de Gestión de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Eliminar estudiante")
        print("3. Buscar estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")

        opcion = input("\nIngrese su opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            eliminar_estudiante()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            mostrar_estudiantes()
        elif opcion == "5":
            print("\nSaliendo del sistema de gestión de estudiantes. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el menú directamente
menu_estudiantes()
