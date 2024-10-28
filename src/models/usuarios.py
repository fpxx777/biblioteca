from config.db import connectToMySQL

class Usuarios:
    
    def __init__(self, data):
        self.id_usuario = data['id_usuario']
        self.nombre = data['nombre']
        self.email = data['email']
        self.contrasena = data['contrasena']

    @classmethod
    def ver_user(cls, email):
        query = f"SELECT * FROM usuarios WHERE email = '{email}';"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def insert_user(cls, email, username, password):
        query = f"INSERT INTO usuarios (nombre, email, contrasena) VALUES ('{username}', '{email}', '{password}')"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
