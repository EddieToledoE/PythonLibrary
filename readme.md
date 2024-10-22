El menú principal tiene las siguientes opciones:
--- Menú Biblioteca Virtual ---

1. Agregar libro
2. Registrar usuario
3. Registrar préstamo
4. Devolver libro
5. Listar todos los usuarios
6. Listar todos los libros
7. Listar todos los préstamos
8. Consultar historial de usuario
9. Salir
   Seleccione una opción:

Opción 1: Agregar Libro
Esta opción permite añadir un nuevo libro a la biblioteca. Deberás proporcionar los siguientes datos:
Nombre del libro: Texto que describe el título del libro.
Autor: Nombre del autor del libro.
Año de publicación: Año en que el libro fue publicado. Debe estar en formato numérico y ser válido (entre 1000 y el año actual).
Categoría: Género o categoría del libro.
Disponibles: Número de ejemplares disponibles. Debe ser un número entero.

Opción 2: Registrar Usuario

Nombre del usuario: Nombre completo del usuario.
Correo electrónico: Debe tener un formato válido (ejemplo: usuario@correo.com).
Teléfono: Número de teléfono del usuario, debe contener exactamente 10 dígitos.
Fecha de registro: Fecha en que el usuario se registra en el formato DD/MM/AA.

Opción 3: Registrar Préstamo

Fecha de préstamo: Fecha en la que se realiza el préstamo en el formato DD/MM/AA.
Fecha de devolución: Fecha en la que se espera la devolución del libro en el formato DD/MM/AA.

Opción 4: Devolver Libro
Esta opción permite registrar la devolución de un libro previamente prestado. Los datos solicitados son:

SKU del Libro: Código único del libro que se está devolviendo.
ID del Préstamo: Identificador del préstamo que se está cerrando.
El sistema actualizará la cantidad de ejemplares disponibles del libro una vez que se haya registrado la devolución.

Opción 5: Listar Todos los Usuarios
Esta opción muestra una lista de todos los usuarios registrados en la base de datos. El sistema mostrará los detalles de cada usuario, tales como el nombre, correo electrónico y teléfono.

Opción 6: Listar Todos los Libros
Esta opción muestra una lista de todos los libros disponibles en la biblioteca. El sistema mostrará detalles como el nombre, SKU, autor, año de publicación y la cantidad de ejemplares disponibles.

Opción 7: Listar Todos los Préstamos
Esta opción muestra una lista de todos los préstamos registrados en el sistema. Se incluye información sobre el usuario que ha solicitado el préstamo, el libro prestado y las fechas de préstamo y devolución.

Opción 8: Consultar Historial de Usuario
Esta opción permite consultar el historial de préstamos de un usuario en particular. Debes proporcionar el ID del Usuario en formato UUID, y el sistema mostrará todos los préstamos asociados a dicho usuario.

Opción 9: Salir
Esta opción cierra el programa.
