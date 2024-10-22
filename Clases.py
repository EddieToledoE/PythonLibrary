
class Libro:
    def __init__(self, nombre, sku, autor, año, categoria, disponibles):
        self.nombre = nombre
        self.sku = sku
        self.autor = autor
        self.año = año
        self.categoria = categoria
        self.disponibles = disponibles


class Usuario:
    def __init__(self, id_usuario, nombre, correo, telefono, fecha_registro):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fecha_registro = fecha_registro


class Prestamo:
    def __init__(self, id_prestamo, id_usuario, sku_libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.sku_libro = sku_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion



def comprobar_disponibilidad_libro(libro):
    if libro.disponibles > 0:
        return True
    else:
        print("El libro no está disponible para préstamo.")
        return False
