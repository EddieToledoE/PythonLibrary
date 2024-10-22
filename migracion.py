import sqlite3
import pandas as pd

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        SKU TEXT UNIQUE,
        Autor TEXT,
        Año INTEGER,
        Categoria TEXT,
        Disponibles INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Usuario TEXT UNIQUE,
        Nombre TEXT,
        Correo_Electronico TEXT,
        Telefono TEXT,
        Fecha_Registro TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prestamos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Prestamo TEXT UNIQUE,
        ID_Usuario TEXT,
        SKU_Libro TEXT,
        Fecha_Prestamo TEXT,
        Fecha_Devolucion TEXT,
        FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
        FOREIGN KEY (SKU_Libro) REFERENCES Libros(SKU)
    )
''')


libros_df = pd.read_csv('libros.csv')
usuarios_df = pd.read_csv('usuarios.csv')
prestamos_df = pd.read_csv('prestamos.csv')


for _, row in libros_df.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO Libros (Nombre, SKU, Autor, Año, Categoria, Disponibles)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (row['Nombre'], row['SKU'], row['Autor'], row['Año'], row['Categoría'], row['Disponibles']))

for _, row in usuarios_df.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO Usuarios (ID_Usuario, Nombre, Correo_Electronico, Telefono, Fecha_Registro)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['ID de Usuario'], row['Nombre'], row['Correo Electrónico'], row['Teléfono'], row['Fecha de Registro']))

for _, row in prestamos_df.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO Prestamos (ID_Prestamo, ID_Usuario, SKU_Libro, Fecha_Prestamo, Fecha_Devolucion)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['ID de Préstamo'], row['ID de Usuario'], row['SKU del Libro'], row['Fecha de Préstamo'], row['Fecha de Devolución']))

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Migración completada exitosamente.")
