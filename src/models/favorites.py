# Importar la función para conectar a la base de datos
from config.db import connectToMySQL
from models.libros import Libros
import math

# Clase para representar a los libros
class Favoritos:
    # Constructor para crear un objeto Libro
    def __init__(self, data):
        # Asignar los valores de la base de datos a los atributos del objeto
        self.id_favorito = data['id_favorito']
        self.id_libro = data['id_libro']
        self.id_usuario = data['id_usuario']


    # Método de clase para obtener todos los libros
    @classmethod
    def insert_book(cls, id_libro, id_usuario):
        query = f"INSERT INTO favoritos (id_libro, id_usuario) VALUES ({id_libro}, {id_usuario});"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def del_book(cls, id_libro, id_usuario):
        query = f"DELETE FROM favoritos WHERE id_libro = {id_libro} AND id_usuario = {id_usuario};"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def verify_book(cls, id_libro, id_usuario):
        query = f"SELECT * FROM favoritos WHERE id_libro = {id_libro} AND id_usuario = {id_usuario};"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def select_all(cls, id_usuario):
        query = f"SELECT * FROM favoritos F LEFT JOIN usuarios U ON F.id_usuario = U.id_usuario LEFT JOIN libros L ON F.id_libro = L.id_libro WHERE U.id_usuario = {id_usuario};"
        results = connectToMySQL('biblionauta').query_db(query)
        books = []
        print(results)
        for book in results:
            books.append(Libros(book))
        return books
