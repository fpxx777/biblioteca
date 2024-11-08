# Importar la función para conectar a la base de datos
from ..config.db import connectToMySQL

# Clase para representar a los géneros de un libro
class Generos:
    # Constructor para crear un objeto Género
    def __init__(self, data):
        # Asignar los valores de la base de datos a los atributos del objeto
        self.id_genero = data['id_genero']  # ID del género
        self.id_libro = data['id_libro']  # ID del libro al que pertenece el género
        self.nombre_genero = data['nombre_genero']  # Nombre del género

    # Método de clase para obtener todos los libros que pertenecen a un género específico
    @classmethod
    def get_all(cls, genero):
        # Crear una consulta SQL para obtener los ID de los libros que pertenecen a un género específico
        query = f'SELECT id_libro FROM generos WHERE nombre_genero = "{genero}";'
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los ID de los libros
        categories = []
        # Iterar sobre los resultados y agregar los ID de los libros a la lista
        for category in results:
            categories.append(category["id_libro"])
        # Regresar la lista de ID de libros
        return categories

    @classmethod
    def get_categories_list(cls):
        # Crear una consulta SQL para obtener la lista de todos los géneros disponibles
        query = f"SELECT DISTINCT nombre_genero FROM generos;"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los nombres de los géneros
        categories = []
        # Iterar sobre los resultados y agregar los nombres de los géneros a la lista
        for category in results:
            categories.append(category["nombre_genero"])
        # Regresar la lista de nombres de géneros
        return categories

    @classmethod
    def get_category(cls, id_libro):
        # Crear una consulta SQL para obtener los géneros de un libro específico
        query = f"SELECT * FROM generos WHERE id_libro = {id_libro};"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los nombres de los géneros
        categories = []
        # Iterar sobre los resultados y agregar los nombres de los géneros a la lista
        for category in results:
            categories.append(category["nombre_genero"])
        # Regresar la lista de nombres de géneros
        return categories
    @classmethod
    def get_categories_list(cls):
        query = "SELECT DISTINCT nombre_genero FROM generos ORDER BY nombre_genero;"
        results = connectToMySQL('biblionauta').query_db(query)
        return [result['nombre_genero'] for result in results]