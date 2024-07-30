# Importar la función para conectar a la base de datos
from config.db import connectToMySQL
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

    # Método de clase para obtener todos los libros
    @classmethod
    def get_all_limit_all(cls, page = 1):
        # Calcula el límite de libros por página
        limit = 12
        # Calcula el offset para la página actual
        offset = (page - 1) * limit
        # Crear una consulta SQL para obtener los libros paginados
        query = f"SELECT * FROM libros LIMIT {limit} OFFSET {offset};"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los objetos Libro
        books = []
        # Iterar sobre los resultados y agregar los objetos Libro a la lista
        for book in results:
            books.append(cls(book))  # Crear un objeto Libro para cada resultado
        # Regresar la lista de objetos Libro y el número total de páginas
        return books

    # Este es un método de clase, lo que significa que pertenece a la clase en sí, en lugar de una instancia de la clase.
    @classmethod
    def get_all(cls):
        # Define una consulta SQL para recuperar todos los libros de la tabla "libros".
        query = "SELECT * FROM libros;"
        
        # Ejecuta la consulta utilizando la función connectToMySQL, que devuelve una lista de resultados.
        results = connectToMySQL('biblionauta').query_db(query)
        
        # Crea una lista vacía para almacenar los objetos de libro.
        books = []
        
        # Itera sobre los resultados, que probablemente son una lista de diccionarios o tuplas.
        for book in results:
            # Para cada resultado, crea una nueva instancia de la clase (cls) y pasa los datos del libro a ella.
            # Esto asume que la clase tiene un método __init__ que toma un diccionario o tupla como argumento.
            books.append(cls(book))
        
        # Devuelve la lista de objetos de libro.
        return books
    # Método para obtener todos los libros de una categoría específica
    def get_all_for_category(cls, category):
        # Crear una consulta SQL para obtener los libros de una categoría específica
        query = f"SELECT * FROM libros WHERE id_libro IN (%s);" % ','.join(map(str, category))
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los objetos Libro
        books = []
        # Iterar sobre los resultados y agregar los objetos Libro a la lista
        for book in results:
            books.append(cls(book))  # Crear un objeto Libro para cada resultado
        # Regresar la lista de objetos Libro
        return books

    # Método para obtener un libro específico por su ID
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
        query = f"SELECT * FROM libros WHERE titulo LIKE '%{letter}%';"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los objetos Libro
        books = []
        # Iterar sobre los resultados y agregar los objetos Libro a la lista
        for book in results:
            books.append(cls(book))  # Crear un objeto Libro para cada resultado
        # Regresar la lista de objetos Libro
        return books