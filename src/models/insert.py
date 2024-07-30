# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
import time
# modelar la clase después de la tabla friend de nuestra base de datos
class Insert:
    # ahora usamos métodos de clase para consultar nuestra base de datos
    # SELECT * FROM tareas ORDER BY (()) ASC LIMIT 50 SKIP 10;
    @classmethod
    def insert_all(cls, book):
        if book:
            if book["imagen"] == 'NA': return False
            else:
                print(book['isbn'])
                query = f"INSERT INTO libros (isbn, titulo, descripcion, paginas, imagen, fecha_publicacion) VALUES ('{book['isbn']}', '{book['titulo']}', '{book['descripcion']}', {book['paginas']}, '{book['imagen']}', '{book['fecha_publicacion']}');"
                connectToMySQL('biblionauta').query_db(query)
                cls.insert_autor(cls, book)
            # crear una lista vacía para agregar nuestras instancias de friends
        else: return False
    def insert_autor(cls, book):
        query = f'SELECT id_libro FROM libros WHERE isbn = "{book["isbn"]}";'
        id_libro = connectToMySQL('biblionauta').query_db(query)
        id_libro = id_libro[0]["id_libro"]
        for autor in book["autores"]:
                query3 = f'INSERT INTO autores (id_libro, nombre_autor) VALUES ({id_libro}, "{autor}")'
                connectToMySQL('biblionauta').query_db(query3)
        for genero in book["generos"]:
                query4 = f'INSERT INTO generos (id_libro, nombre_genero) VALUES ({id_libro}, "{genero}")'
                connectToMySQL('biblionauta').query_db(query4)
