# Lista para almacenar los libros
libreria = []

# Función para agregar un libro
def agregar_libro():
    titulo = input("\nIngrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    cantidad = int(input("Ingrese la cantidad de libros disponibles: "))

    libro = {"titulo": titulo, "autor": autor, "cantidad": cantidad}
    libreria.append(libro)
    print(f"\nEl libro '{titulo}' ha sido agregado a la librería.")

# Función para eliminar un libro
def eliminar_libro():
    titulo = input("\nIngrese el título del libro que desea eliminar: ")
    for libro in libreria:
        if libro["titulo"].lower() == titulo.lower():
            libreria.remove(libro)
            print(f"\nEl libro '{titulo}' ha sido eliminado.")
            return
    print(f"\nEl libro '{titulo}' no se encontró en la librería.")

# Función para buscar un libro
def buscar_libro():
    titulo = input("\nIngrese el título del libro que desea buscar: ")
    for libro in libreria:
        if libro["titulo"].lower() == titulo.lower():
            print(f"\nLibro encontrado: Título: {libro['titulo']}, Autor: {libro['autor']}, Cantidad: {libro['cantidad']}")
            return
    print(f"\nEl libro '{titulo}' no se encontró en la librería.")

# Función para mostrar todos los libros
def mostrar_libreria():
    if libreria:
        print("\nLibros disponibles en la librería:")
        for libro in libreria:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Cantidad: {libro['cantidad']}")
    else:
        print("\nLa librería está vacía.")

# Menú principal
def menu_libreria():
    while True:
        print("\n--- Sistema de Gestión de Librería ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Mostrar todos los libros")
        print("5. Salir")

        opcion = input("\nIngrese su opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            eliminar_libro()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            mostrar_libreria()
        elif opcion == "5":
            print("\nSaliendo del sistema de gestión de librería. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el menú directamente
menu_libreria()
