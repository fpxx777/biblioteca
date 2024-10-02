# Importar la biblioteca Flask para crear una aplicación web
from flask import Flask, render_template, request, session

# Importar modelos de datos para libros, géneros, autores y inserción de datos
from models.libros import Libros  # Modelo para libros
from models.generos import Generos  # Modelo para géneros
from models.autores import Autores  # Modelo para autores
from models.insert import Insert  # Modelo para inserción de datos

# Importar función para obtener información de un libro a partir de su ISBN
from prueba import get_book_info  # Función para obtener información de un libro

# Crear una aplicación Flask
app = Flask(__name__)

# Ruta raíz de la aplicación (index)
@app.route("/", methods=["GET", "POST"])
def index():
    # Obtener todos los libros
    books = Libros.get_all_limit_all(1)
    # Renderizar la plantilla index.html con la lista de libros y categorías
    return render_template("index.html", books=books)

# Ruta para búsqueda de libros
@app.route("/search/", methods=["GET", "POST"])
def search():
    # Obtener el término de búsqueda de la solicitud
    search = request.args.get("search")
    # Buscar libros que coinciden con el término de búsqueda
    books = Libros.search(search)
    # Renderizar la plantilla search.html con la lista de libros encontrados
    return render_template("search.html", books=books, search=search)

# Ruta para mostrar categorías de libros
@app.route("/categories", methods=["GET"])
def categories(): # Obtener la página actual
    books = Libros.get_all()  # Obtener los libros paginados
    # Obtener la lista de categorías
    categories = Generos.get_categories_list(Generos)
    # Establecer la categoría actual como "Libros destacados"
    category = "Libros destacados"
    # Renderizar la plantilla categories.html con la lista de libros y categorías
    return render_template("categories.html", category=category, books=books, categories=categories)

# Ruta para mostrar libros de una categoría específica
@app.route("/category/<category>", methods=["GET"])
def categorie(category):
    # Obtener la lista de libros de la categoría específica
    category_for_book = Generos.get_all(category)
    # Obtener la lista de libros que pertenecen a la categoría
    books = Libros.get_all_for_category(Libros, category_for_book)
    # Obtener la lista de categorías
    categories = Generos.get_categories_list(Generos)
    # Renderizar la plantilla categories.html con la lista de libros y categorías
    return render_template("categories.html", category=category, books=books, categories=categories, category_for_book=category_for_book)

# Ruta para mostrar información de un libro específico
@app.route("/book/<bookid>/", methods=["GET"])
def a(bookid):
    # Obtener el libro específico
    book = Libros.get_book(Libros, bookid)
    # Obtener la lista de autores del libro
    authors = Autores.get_all(bookid)
    # Obtener la categoría del libro
    categories = Generos.get_category(Generos, bookid)
    print(categories)  # Imprimir la categoría del libro para depuración
    # Renderizar la plantilla book.html con la información del libro
    return render_template("book.html", book=book, authors=authors, categories=categories)

# Ruta para probar la inserción de datos
@app.route("/test", methods=["GET", "POST"])
def test():
    # Si se envía una solicitud POST, procesar la inserción de datos
    if request.method == "POST":
        # Obtener el ISBN del libro
        response = request.form.get("isbn")
        # Obtener la información del libro a partir del ISBN
        book = get_book_info(response)
        # Si se obtuvo la información del libro, insertar los datos
        if len(book) == 2:
            return render_template("insert-error.html")
        else:
            print("aaaaaaaaaaa")
    # Renderizar la plantilla insert.html para probar la inserción de datos
    return render_template("insert.html")

# Iniciar la aplicación Flask en modo depuración
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)