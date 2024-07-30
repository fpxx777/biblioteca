# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Generos:
    def __init__( self , data ):
        self.id_genero = data['id_genero']
        self.id_libro = data['id_libro']
        self.nombre_genero = data['nombre_genero']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    # SELECT * FROM tareas ORDER BY (()) ASC LIMIT 50 SKIP 10;
    @classmethod
    def get_all(cls, genero):
        query = f'SELECT id_libro FROM generos WHERE nombre_genero = "{genero}";'
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        categories = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for category in results:
            print(category)
            categories.append( category["id_libro"] )
        return categories
    def get_categories_list(cls):
        query = f"SELECT DISTINCT nombre_genero FROM generos;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        categories = []
        print(results)
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for category in results:
                categories.append(category["nombre_genero"])
        return categories
    def get_category(cls, id_libro):
        query = f"SELECT * FROM generos WHERE id_libro = {id_libro};"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        categories = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for category in results:
            categories.append( category["nombre_genero"] )
        return categories