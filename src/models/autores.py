# Importar la función para conectar a la base de datos
from ..config.db import connectToMySQL

# Clase para representar a los autores de un libro
class Autores:
    # Constructor para crear un objeto Autor
    def __init__(self, data):
        # Asignar los valores de la base de datos a los atributos del objeto
        self.id_genero = data['id_libro']  # ID del género (no utilizado en este caso)
        self.id_libro = data['id_libro']  # ID del libro al que pertenece el autor
        self.nombre_autor = data['nombre_autor']  # Nombre del autor

    # Método de clase para obtener todos los autores de un libro
    @classmethod
    def get_all(cls, id_libro):
        # Crear una consulta SQL para obtener todos los autores de un libro
        query = f"SELECT * FROM autores WHERE id_libro = {id_libro}"
        # Ejecutar la consulta SQL y obtener los resultados
        results = connectToMySQL('biblionauta').query_db(query)
        # Crear una lista para almacenar los nombres de los autores
        authors = []
        # Iterar sobre los resultados y agregar los nombres de los autores a la lista
        for author in results:
            authors.append(author["nombre_autor"])
        # Regresar la lista de nombres de autores
        return authors
    @classmethod
    def get_all_authors(cls):
        query = "SELECT DISTINCT nombre_autor FROM autores ORDER BY nombre_autor;"
        results = connectToMySQL('biblionauta').query_db(query)
        return [result['nombre_autor'] for result in results]
