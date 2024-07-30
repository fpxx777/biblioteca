# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Autores:
    def __init__( self , data ):
        self.id_genero = data['id_libro']
        self.id_libro = data['id_libro']
        self.nombre_autor = data['nombre_autor']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    # SELECT * FROM tareas ORDER BY (()) ASC LIMIT 50 SKIP 10;
    @classmethod
    def get_all(cls, id_libro):
        query = f"SELECT * FROM autores WHERE id_libro = {id_libro}"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        authors = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for author in results:
            authors.append( author["nombre_autor"] )
        return authors