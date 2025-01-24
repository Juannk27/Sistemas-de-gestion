# Lista para almacenar el inventario
inventario = []

# Función para agregar un producto al inventario
def agregar_producto():
    nombre = input("\nIngrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))

    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
    print(f"\nEl producto '{nombre}' ha sido agregado al inventario.")

# Función para eliminar un producto del inventario
def eliminar_producto():
    nombre = input("\nIngrese el nombre del producto que desea eliminar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print(f"\nEl producto '{nombre}' ha sido eliminado del inventario.")
            return
    print(f"\nEl producto '{nombre}' no se encontró en el inventario.")

# Función para buscar un producto en el inventario
def buscar_producto():
    nombre = input("\nIngrese el nombre del producto que desea buscar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"\nProducto encontrado: Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}")
            return
    print(f"\nEl producto '{nombre}' no se encontró en el inventario.")

# Función para mostrar todos los productos del inventario
def mostrar_inventario():
    if inventario:
        print("\nProductos disponibles en el inventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}")
    else:
        print("\nEl inventario está vacío.")

# Menú principal
def menu_inventario():
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("\nIngrese su opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            print("\nSaliendo del sistema de gestión de inventario. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el menú directamente
menu_inventario()
