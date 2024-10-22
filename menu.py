from MetodosBd import *

def mostrar_menu():
    print("\n--- Menú Biblioteca Virtual ---")
    print("1. Agregar libro")
    print("2. Registrar usuario")
    print("3. Registrar préstamo")
    print("4. Devolver libro")
    print("5. Listar todos los usuarios")
    print("6. Listar todos los libros")
    print("7. Listar todos los préstamos")
    print("8. Consultar historial de usuario")
    print("9. Salir")
    return input("Seleccione una opción: ")


def registrar_prestamo_con_seleccion():
    
    print("Usuarios disponibles:")
    cursor.execute('SELECT ID_Usuario, Nombre FROM Usuarios')
    usuarios = cursor.fetchall()
    
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    else:
        for index, usuario in enumerate(usuarios):
            print(f"{index + 1}. {usuario[1]} (ID: {usuario[0]})")
        
        seleccion_usuario = input(f"Seleccione el número del usuario (1-{len(usuarios)}): ")
        
        if seleccion_usuario.isdigit() and 1 <= int(seleccion_usuario) <= len(usuarios):
            usuario_seleccionado = usuarios[int(seleccion_usuario) - 1]
            id_usuario = usuario_seleccionado[0]
            print(f"Usuario seleccionado: {usuario_seleccionado[1]} (ID: {id_usuario})")
        else:
            print("Selección no válida.")
            return

  
    print("Libros disponibles:")
    cursor.execute('SELECT SKU, Nombre FROM Libros')
    libros = cursor.fetchall()
    
    if not libros:
        print("No hay libros disponibles.")
        return
    else:
        for index, libro in enumerate(libros):
            print(f"{index + 1}. {libro[1]} (SKU: {libro[0]})")
        
        seleccion_libro = input(f"Seleccione el número del libro (1-{len(libros)}): ")
        
        if seleccion_libro.isdigit() and 1 <= int(seleccion_libro) <= len(libros):
            libro_seleccionado = libros[int(seleccion_libro) - 1]
            sku_libro = libro_seleccionado[0]
            print(f"Libro seleccionado: {libro_seleccionado[1]} (SKU: {sku_libro})")
        else:
            print("Selección no válida.")
            return

   
    fecha_prestamo = input("Ingrese la fecha de préstamo (DD/MM/AA): ")
    fecha_devolucion = input("Ingrese la fecha de devolución (DD/MM/AA): ")
    
   
    registrar_prestamo(id_usuario, sku_libro, fecha_prestamo, fecha_devolucion)

def devolver_libro_con_seleccion():
  
    print("Libros disponibles:")
    cursor.execute('SELECT SKU, Nombre FROM Libros')
    libros = cursor.fetchall()
    
    if not libros:
        print("No hay libros disponibles.")
        return
    else:
        for index, libro in enumerate(libros):
            print(f"{index + 1}. {libro[1]} (SKU: {libro[0]})")
        
        seleccion_libro = input(f"Seleccione el número del libro (1-{len(libros)}): ")
        
        if seleccion_libro.isdigit() and 1 <= int(seleccion_libro) <= len(libros):
            libro_seleccionado = libros[int(seleccion_libro) - 1]
            sku_libro = libro_seleccionado[0]
            print(f"Libro seleccionado: {libro_seleccionado[1]} (SKU: {sku_libro})")
        else:
            print("Selección no válida.")
            return

   
    print(f"Préstamos asociados al libro {libro_seleccionado[1]}:")
    cursor.execute('SELECT ID_Prestamo, ID_Usuario FROM Prestamos WHERE SKU_Libro = ?', (sku_libro,))
    prestamos = cursor.fetchall()
    
    if not prestamos:
        print(f"No hay préstamos registrados para el libro {libro_seleccionado[1]}.")
        return
    else:
        for index, prestamo in enumerate(prestamos):
            print(f"{index + 1}. Préstamo ID: {prestamo[0]} (ID Usuario: {prestamo[1]})")
        
        seleccion_prestamo = input(f"Seleccione el número del préstamo (1-{len(prestamos)}): ")
        
        if seleccion_prestamo.isdigit() and 1 <= int(seleccion_prestamo) <= len(prestamos):
            prestamo_seleccionado = prestamos[int(seleccion_prestamo) - 1]
            id_prestamo = prestamo_seleccionado[0]
            print(f"Préstamo seleccionado: {id_prestamo} (ID Usuario: {prestamo_seleccionado[1]})")
        else:
            print("Selección no válida.")
            return

   
    devolver_libro(sku_libro, id_prestamo)
    print(f"Libro con SKU {sku_libro} devuelto exitosamente.")




def consultar_historial_usuario_con_seleccion():
   
    print("Usuarios disponibles:")
    cursor.execute('SELECT ID_Usuario, Nombre FROM Usuarios')
    usuarios = cursor.fetchall()
    
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    else:
        for index, usuario in enumerate(usuarios):
            print(f"{index + 1}. {usuario[1]} (ID: {usuario[0]})")
        
        seleccion_usuario = input(f"Seleccione el número del usuario (1-{len(usuarios)}): ")
        
        if seleccion_usuario.isdigit() and 1 <= int(seleccion_usuario) <= len(usuarios):
            usuario_seleccionado = usuarios[int(seleccion_usuario) - 1]
            id_usuario = usuario_seleccionado[0]
            print(f"Usuario seleccionado: {usuario_seleccionado[1]} (ID: {id_usuario})")
        else:
            print("Selección no válida.")
            return

    
    consultar_historial_usuario(id_usuario)



def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del libro: ")
            autor = input("Ingrese el autor del libro: ")
            anio = input("Ingrese el año de publicación: ")
            categoria = input("Ingrese la categoría del libro: ")
            disponibles = input("Ingrese el número de copias disponibles: ")
            agregar_libro(nombre, autor, anio, categoria, disponibles)
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo electrónico del usuario: ")
            telefono = input("Ingrese el teléfono del usuario: ")
            fecha_registro = input("Ingrese la fecha de registro (DD/MM/AA): ")
            registrar_usuario( nombre, correo, telefono, fecha_registro)
        
        elif opcion == '3':
            registrar_prestamo_con_seleccion()
            
        elif opcion == '4':
            devolver_libro_con_seleccion()
        
        elif opcion == '5':
            listar_usuarios()
        
        elif opcion == '6':
            listar_libros()
        
        elif opcion == '7':
            listar_prestamos()
        
        elif opcion == '8':
            consultar_historial_usuario_con_seleccion()
        
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
