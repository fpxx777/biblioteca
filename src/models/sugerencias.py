from config.db import connectToMySQL

class Sugerencia:
    def __init__(self, data):
        # Asignar los valores de la base de datos a los atributos del objeto
        self.id_sugerencia = data['id_sugerencia']  # ID de la sugerencia
        self.titulo = data['titulo']  # Título de la sugerencia
        self.autor = data['autor']  # Autor de la sugerencia
        self.isbn = data.get('isbn')  # ISBN de la sugerencia (opcional)
        self.ano = data['ano']  # Año de la sugerencia (timestamp)
        self.razon = data['razon']  # Razón de la sugerencia

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sugerencias"
        results = connectToMySQL('biblionauta').query_db(query)
        sugerencias = []
        for sugerencia in results:
            sugerencias.append(cls(sugerencia))
        return sugerencias
    @classmethod
    def add_request(cls, data):
        if not data["isbn"]:
            data["isbn"] = 0
        if not data["year"]:
            data["year"] = "NULL"
        if not data["reason"]:
            data["reason"] = "NULL"
        query = f"INSERT INTO sugerencias (titulo, autor, isbn, ano, razon) VALUES ('{data['title']}', '{data['author']}', {data['isbn']}, {data['year']}, '{data['reason']}')"
        results = connectToMySQL('biblionauta').query_db(query)
        return results
