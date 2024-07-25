# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Tarea:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tareas ORDER BY (()) ASC LIMIT 50 SKIP 10;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('tareas').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends