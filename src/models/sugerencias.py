from ..config.db import connectToMySQL

class Sugerencia:
    def __init__(self, data):
        self.id_sugerencia = data['id_sugerencia']  
        self.titulo = data['titulo']  
        self.autor = data['autor']  
        self.isbn = data.get('isbn')  
        self.ano = data['ano']  
        self.razon = data['razon']  
        self.id_usuario = data['id_usuario']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sugerencias JOIN usuarios ON sugerencias.id_usuario = usuarios.id_usuario;"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def add_request(cls, data):
        if not data["isbn"]:
            data["isbn"] = 0
        if not data["year"]:
            data["year"] = "NULL"
        if not data["reason"]:
            data["reason"] = "NULL"
        query = f"INSERT INTO sugerencias (titulo, autor, isbn, ano, razon, id_usuario) VALUES ('{data['title']}', '{data['author']}', {data['isbn']}, {data['year']}, '{data['reason']}', {data['id_usuario']});"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
    @classmethod
    def del_request(cls, id_sugerencia):
        query = f"DELETE FROM sugerencias WHERE id_sugerencia = {id_sugerencia}"
        results = connectToMySQL('biblionauta').query_db(query)
        return results