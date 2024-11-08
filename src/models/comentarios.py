from ..config.db import connectToMySQL

class Comentario:
    def __init__(self, data):
        self.id_comentario = data["id_comentario"]
        self.id_usuario = data["id_usuario"]
        self.id_libro = data["id_libro"]
        self.texto = data["texto"]
        self.estrellas = data["estrellas"]

        self.nombre = data['nombre']
        self.email = data['email']
        self.contrasena = data['contrasena']
        self.img = data['img']
        self.created_at = data['created_at']
        self.rango = data["rango"]
    
    @classmethod
    def get_commets(cls, id_libro):
        query = f"SELECT * FROM comentarios JOIN usuarios ON comentarios.id_usuario = usuarios.id_usuario WHERE id_libro = {id_libro};"
        results = connectToMySQL('biblionauta').query_db(query)
        comentarios = []
        for comentario in results:
            comentarios.append(cls(comentario))
        return comentarios
    @classmethod
    def add_comment(cls, id_libro, id_usuario, texto, estrellas):
        query = f"INSERT INTO comentarios (id_libro, id_usuario, texto, estrellas) VALUES ({id_libro}, {id_usuario}, '{texto}', {estrellas});"
        results = connectToMySQL('biblionauta').query_db(query)
        return results