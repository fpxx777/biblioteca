# Importar la función para conectar a la base de datos
from config.db import connectToMySQL

# Importar la función para obtener la hora actual
import time

# Clase para insertar datos en la base de datos
class Insert:
    # Método para insertar un libro en la base de datos
    @classmethod
    def insert_all(cls, book):
        # Verificar si el libro tiene información válida
        if book:
            # Verificar si el libro tiene una imagen asociada
            if book["imagen"] == 'NA':
                # Si no tiene imagen, regresar False
                return False
            else:
                # Crear una consulta SQL para insertar el libro en la base de datos
                query = f"INSERT INTO libros (isbn, titulo, descripcion, paginas, imagen, fecha_publicacion) VALUES ('{book['isbn']}', '{book['titulo']}', '{book['descripcion']}', {book['paginas']}, '{book['imagen']}', '{book['fecha_publicacion']}');"
                # Ejecutar la consulta SQL para insertar el libro
                connectToMySQL('biblionauta').query_db(query)
                # Llamar al método para insertar los autores del libro
                cls.insert_autor(cls, book)
        else:
            # Si el libro no tiene información válida, regresar False
            return False

    # Método para insertar los autores de un libro en la base de datos
    def insert_autor(cls, book):
        # Crear una consulta SQL para obtener el ID del libro recién insertado
        query = f'SELECT id_libro FROM libros WHERE isbn = "{book["isbn"]}";'
        # Ejecutar la consulta SQL para obtener el ID del libro
        id_libro = connectToMySQL('biblionauta').query_db(query)
        # Obtener el ID del libro como un entero
        id_libro = id_libro[0]["id_libro"]
        # Iterar sobre los autores del libro
        for autor in book["autores"]:
            # Crear una consulta SQL para insertar el autor en la base de datos
            query3 = f'INSERT INTO autores (id_libro, nombre_autor) VALUES ({id_libro}, "{autor}")'
            # Ejecutar la consulta SQL para insertar el autor
            connectToMySQL('biblionauta').query_db(query3)
        # Iterar sobre los géneros del libro
        for genero in book["generos"]:
            # Crear una consulta SQL para insertar el género en la base de datos
            query4 = f'INSERT INTO generos (id_libro, nombre_genero) VALUES ({id_libro}, "{genero}")'
            # Ejecutar la consulta SQL para insertar el género
            connectToMySQL('biblionauta').query_db(query4)