from config.db import connectToMySQL

class Usuarios:
    
    def __init__(self, data):
        self.id_usuario = data['id_usuario']
        self.nombre = data['nombre']
        self.email = data['email']
        self.contrasena = data['contrasena']
        self.img = data['img']
        self.created_at = data['created_at']
        self.rango = data["rango"]

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
    @classmethod
    def insert_img(cls, id_usuario, img):
        print(img)
        query = f"UPDATE usuarios SET img = '{img}' WHERE id_usuario = {id_usuario};"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def new_name(cls, id_usuario, new_name):
        query = f"UPDATE usuarios SET nombre = '{new_name}' WHERE id_usuario = {id_usuario}"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
