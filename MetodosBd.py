import sqlite3
import re
import uuid
import random
from datetime import datetime



# Conexión a la base de datos SQLite
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Validaciones
def validar_uuid(uuid_str):
    regex = r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    return re.match(regex, uuid_str) is not None

def validar_correo(correo):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, correo) is not None

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, '%d/%m/%y')
        return True
    except ValueError:
        return False

def validar_sku(sku):
    return sku.isdigit()

def validar_anio(anio):
    return anio.isdigit() and 1000 <= int(anio) <= datetime.now().year

def validar_disponibles(disponibles):
    return disponibles.isdigit()

def generar_sku():
    return str(random.randint(1000000000000, 9999999999999))  # Generar un SKU de 13 dígitos


def agregar_libro(nombre,autor, anio, categoria, disponibles):
    sku = generar_sku()  # Generar SKU automáticamente
    if not validar_anio(anio):
        print(f"El año debe ser un número válido entre 1000 y {datetime.now().year}.")
        return
    if not validar_disponibles(disponibles):
        print("La cantidad de disponibles debe ser un número entero.")
        return
    
    cursor.execute('''
        INSERT INTO Libros (Nombre, SKU, Autor, Año, Categoria, Disponibles)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, sku, autor, anio, categoria, disponibles))
    conn.commit()
    print(f"Libro {nombre} agregado exitosamente.")

def registrar_usuario(nombre, correo, telefono, fecha_registro):
    
    id_usuario = str(uuid.uuid4())
    if not validar_correo(correo):
        print("Correo electrónico no válido.")
        return
    if not validar_telefono(telefono):
        print("El teléfono debe ser un número de 10 dígitos.")
        return
    if not validar_fecha(fecha_registro):
        print("Fecha de registro no válida. Use el formato DD/MM/AA.")
        return
    
    cursor.execute('''
        INSERT INTO Usuarios (ID_Usuario, Nombre, Correo_Electronico, Telefono, Fecha_Registro)
        VALUES (?, ?, ?, ?, ?)
    ''', (id_usuario, nombre, correo, telefono, fecha_registro))
    conn.commit()
    print(f"Usuario {nombre} registrado exitosamente.")

def registrar_prestamo( id_usuario, sku_libro, fecha_prestamo, fecha_devolucion):
    id_prestamo = str(uuid.uuid4())
    if not validar_uuid(id_usuario):
        print("ID de Usuario no válido.")
        return
    if not validar_sku(sku_libro):
        print("El SKU del libro debe ser numérico.")
        return
    if not validar_fecha(fecha_prestamo) or not validar_fecha(fecha_devolucion):
        print("Las fechas deben tener el formato DD/MM/AA.")
        return

    # Comprobando disponibilidad del libro
    cursor.execute('SELECT Disponibles FROM Libros WHERE SKU = ?', (sku_libro,))
    libro = cursor.fetchone()
    if libro and libro[0] > 0:
        cursor.execute('''
            INSERT INTO Prestamos (ID_Prestamo, ID_Usuario, SKU_Libro, Fecha_Prestamo, Fecha_Devolucion)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_prestamo, id_usuario, sku_libro, fecha_prestamo, fecha_devolucion))
        cursor.execute('UPDATE Libros SET Disponibles = Disponibles - 1 WHERE SKU = ?', (sku_libro,))
        conn.commit()
        print("Préstamo registrado exitosamente.")
    else:
        print("El libro no está disponible.")

def devolver_libro(sku_libro, id_prestamo):
    if not validar_sku(sku_libro):
        print("El SKU del libro debe ser numérico.")
        return
    if not validar_uuid(id_prestamo):
        print("ID de Préstamo no válido.")
        return

    cursor.execute('DELETE FROM Prestamos WHERE ID_Prestamo = ?', (id_prestamo,))
    cursor.execute('UPDATE Libros SET Disponibles = Disponibles + 1 WHERE SKU = ?', (sku_libro,))
    conn.commit()
    print("Libro devuelto exitosamente.")

def listar_usuarios():
    cursor.execute('SELECT * FROM Usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

def listar_libros():
    cursor.execute('SELECT * FROM Libros')
    libros = cursor.fetchall()
    for libro in libros:
        print(libro)

def listar_prestamos():
    cursor.execute('SELECT * FROM Prestamos')
    prestamos = cursor.fetchall()
    for prestamo in prestamos:
        print(prestamo)

def consultar_historial_usuario(id_usuario):
    cursor.execute('SELECT * FROM Prestamos WHERE ID_Usuario = ?', (id_usuario,))
    historial = cursor.fetchall()
    for prestamo in historial:
        print(prestamo)
