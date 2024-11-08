# Importar la función para conectar a la base de datos
from ..config.db import connectToMySQL
from .generos import Generos
import math

# Clase para representar a los libros
class Libros:
    # Constructor para crear un objeto Libro
    def __init__(self, data):
        # Asignar los valores de la base de datos a los atributos del objeto
        self.id_libro = data['id_libro']  # ID del libro
        self.isbn = data['isbn']  # ISBN del libro
        self.titulo = data['titulo']  # Título del libro
        self.descripcion = data['descripcion']  # Descripción del libro
        self.paginas = data['paginas']  # Número de páginas del libro
        self.imagen = data['imagen']  # Imagen del libro
        self.fecha_publicacion = data['fecha_publicacion']  # Fecha de publicación del libro
        self.nombre_autor = [data["nombre_autor"]]

    # Método de clase para obtener todos los libros
    @classmethod
    def get_all_limit_all(cls, page, limit):
        offset = (page - 1) * limit
        query = f"SELECT * FROM libros LEFT JOIN autores ON libros.id_libro = autores.id_libro LIMIT {limit} OFFSET {offset};"
        results = connectToMySQL('biblionauta').query_db(query)
        books = []
        print(results)
        for book in results:
            existing_book = next((b for b in books if b.id_libro == book["id_libro"]), None)
            if existing_book:
                existing_book.nombre_autor.append(book["nombre_autor"])
            else:
                books.append(cls(book))
        return books

    # Este es un método de clase, lo que significa que pertenece a la clase en sí, en lugar de una instancia de la clase.
    @classmethod
    def get_all(cls):
        # Define una consulta SQL para recuperar todos los libros de la tabla "libros".
        query = "SELECT * FROM libros;"
        
        # Ejecuta la consulta utilizando la función connectToMySQL, que devuelve una lista de resultados.
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def get_all_for_category(cls, category):
        # Crear una consulta SQL para obtener los libros de una categoría específica
        query = f"SELECT * FROM libros LEFT JOIN autores ON libros.id_libro = autores.id_libro WHERE libros.id_libro IN (%s);" % ','.join(map(str, category))
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los objetos Libro
        books = []
        # Iterar sobre los resultados y agregar los objetos Libro a la lista
        for book in results:
            existing_book = next((b for b in books if b.id_libro == book["id_libro"]), None)
            if existing_book:
                existing_book.nombre_autor.append(book["nombre_autor"])
            else:
                books.append(cls(book))
        return books

    @classmethod
    def get_book(cls, bookid):
        # Crear una consulta SQL para obtener un libro específico por su ID
        query = f"SELECT * FROM libros WHERE id_libro = {int(bookid)};"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Regresar los resultados (no se crea un objeto Libro en este caso)
        return results

    # Método de clase para buscar libros por título
    @classmethod
    def search(cls, letter):
        # Crear una consulta SQL para buscar libros por título
        query = f"SELECT * FROM libros LEFT JOIN autores ON libros.id_libro = autores.id_libro WHERE libros.titulo LIKE '%{letter}%';"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los objetos Libro
        books = []
        # Iterar sobre los resultados y agregar los objetos Libro a la lista
        for book in results:
            existing_book = next((b for b in books if b.id_libro == book["id_libro"]), None)
            if existing_book:
                existing_book.nombre_autor.append(book["nombre_autor"])
            else:
                books.append(cls(book))
        return books
    @classmethod
    def get_publication_years(cls):
        query = "SELECT DISTINCT YEAR(fecha_publicacion) as year FROM libros ORDER BY year DESC;"
        results = connectToMySQL('biblionauta').query_db(query)
        return [str(result['year']) for result in results]