from flask import Flask, render_template, request, redirect, session, send_from_directory
from flask_bcrypt import Bcrypt
from datetime import datetime
import math
import os

# Importar modelos de datos para libros, géneros, autores y inserción de datos
from models.libros import Libros  # Modelo para libros
from models.generos import Generos  # Modelo para géneros
from models.autores import Autores  # Modelo para autores
from models.insert import Insert  # Modelo para inserción de datos
from models.favorites import Favoritos
from models.usuarios import Usuarios
from models.sugerencias import Sugerencia

# Importar función para obtener información de un libro a partir de su ISBN
from prueba import get_book_info  # Función para obtener información de un libro

# Crear una aplicación Flask
app = Flask(__name__)

app.secret_key = "P4S$W0rd"

bcrypt = Bcrypt(app)


@app.route("/logout/", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")

# Ruta raíz de la aplicación (index)
@app.route("/", methods=["GET", "POST"])
def index():
    # Obtener todos los libros
    books = Libros.get_all_limit_all(1, 12)
    # Renderizar la plantilla index.html con la lista de libros y categorías
    return render_template("index.html", books=books, session=session)

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
@app.route("/categories/<page>/", methods=["GET"])
def categories(page): # Obtener la página actual
    generos = Generos.get_categories_list()
    autores = Autores.get_all_authors()
    fechas = Libros.get_publication_years()
    total_pages = len(Libros.get_all()) / 24
    total_pages = math.ceil(total_pages)
    books = Libros.get_all_limit_all(int(page), 25)  # Obtener los libros paginados
    # Obtener la lista de categorías
    categories = Generos.get_categories_list()
    # Establecer la categoría actual como "Libros destacados"
    category = "Libros destacados"
    # Renderizar la plantilla categories.html con la lista de libros y categorías
    return render_template("categories.html", category=category, books=books, categories=categories, page=int(page), total_pages=total_pages, generos=generos, autores=autores, fechas=fechas)


# Ruta para mostrar libros de una categoría específica
@app.route("/category/<name>/<page>/", methods=["GET"])
def categorie(name, page):
    generos = Generos.get_categories_list()
    autores = Autores.get_all_authors()
    fechas = Libros.get_publication_years()
    # Obtener la lista de libros de la categoría específica
    category_for_book = Generos.get_all(name)
    print(category_for_book)
    # Obtener la lista de libros que pertenecen a la categoría
    books = Libros.get_all_for_category(category_for_book)
    # Obtener la lista de categorías
    categories = Generos.get_categories_list()
    # Renderizar la plantilla categories.html con la lista de libros y categorías
    return render_template("categories.html", books=books, categories=categories, category_for_book=category_for_book, page=int(page), total_pages=1, generos=generos, autores=autores, fechas=fechas)

# Ruta para mostrar información de un libro específico
@app.route("/book/<bookid>/", methods=["GET"])
def book(bookid):
    book = Libros.get_book(bookid)
    # Obtener la lista de autores del libro
    authors = Autores.get_all(bookid)
    # Obtener la categoría del libro
    categories = Generos.get_category(bookid)
    if session:
        is_book = Favoritos.verify_book(bookid, session["id"])
        if len(is_book) > 0:
            is_book = True
        else:
            is_book = False
        return render_template("book.html", book=book, authors=authors, categories=categories, is_book=is_book)
    else:
        return render_template("book.html", book=book, authors=authors, categories=categories)

# Ruta para probar la inserción de datos
@app.route("/test/", methods=["GET", "POST"])
def test():
    # Si se envía una solicitud POST, procesar la inserción de datos
    if request.method == "POST":
        # Obtener el ISBN del libro
        response = request.form.get("isbn")
        # Obtener la información del libro a partir del ISBN
        errors, book = get_book_info(response)
        # Si se obtuvo la información del libro, insertar los datos
        if errors:
            return render_template("insert-error.html", isbn= book["isbn"], book=book, errors=errors)
        else:
            return redirect("/")
    # Renderizar la plantilla insert.html para probar la inserción de datos
    return render_template("insert.html")

@app.route("/test/fill/", methods=["POST"])
def fill():
    response = request.form.to_dict()
    if 'autores' in response and response['autores']:
        response['autores'] = [autor.strip() for autor in response['autores'].split(',')] if response['autores'] else []
    if 'generos' in response and response['generos']:
        response['generos'] = [genero.strip() for genero in response['generos'].split(',')] if response['generos'] else []
    book = get_book_info(response["isbn"], response)
    print(book)
    return redirect("/test/")

@app.route("/favorites/", methods=["GET"])
def favorites():
    if session:
        books = Favoritos.select_all(session["id"])
        return render_template("favorites.html", books=books)
    else:
        return redirect("/login&register")

@app.route("/favorites/add/", methods=["POST"])
def add():
    id_book = request.form.get("id-book")
    is_book = Favoritos.verify_book(id_book, session["id"])
    if len(is_book) > 0:
        Favoritos.del_book(id_book, session["id"])
    else:
        Favoritos.insert_book(id_book, session['id'])
    return redirect("/favorites/")
# Iniciar la aplicación Flask en modo depuración

@app.route("/login&register", methods=["GET"])
def login_register():
    return render_template("login&register.html")

@app.route('/register/', methods=['POST'])
def register():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password").strip()
    confirm_password = request.form.get("confirm-password").strip()
    errors = []
    
    is_email = Usuarios.ver_user(email)
    if len(is_email) > 0:
        errors.append("existe")
    elif password != confirm_password:
        errors.append("no igual")
    
    if len(errors) > 0:
        return render_template("login&register.html", errors=errors)
    else:
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        Usuarios.insert_user(email, username, hashed_password)
        return redirect("/")

@app.route('/login/', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    errors = []
    
    user = Usuarios.ver_user(email)
    if len(user) != 1:
        errors.append("no register")
        return render_template("login&register.html", errors=errors)
    
    user = user[0]
    if not bcrypt.check_password_hash(user["contrasena"], password):
        errors.append("mal")
        return render_template("login&register.html", errors=errors)
    else:
        if user["rango"] == 'admin':
            session["rango"] = "admin"
        session["id"] = user["id_usuario"]
        session["username"] = user["nombre"]
        session["img"] = user["img"]
        session["gmail"] = user["email"]
        datetime_object = datetime.strptime(str(user["created_at"]), "%Y-%m-%d %H:%M:%S")
        date_only = datetime_object.strftime('%Y-%m-%d')
        session['created_at'] = date_only
        return redirect("/")
    
@app.route("/profile/", methods=["GET"])
def profile():
    return render_template("edit-user.html", session=session)


MEDIA_FOLDER = "media/"
app.config["UPLOAD_FOLDER"] = MEDIA_FOLDER

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )

@app.route("/profile/change/", methods=["POST"])
def edit_profile():
    print("aki",request.files)
    if "file" in request.files:
        file = request.files["file"]
        if file.filename:
            filename = file.filename
            path = os.path.join(MEDIA_FOLDER, filename)
            file.save(path)
            print(f"Imagen guardada en: {path}") 
            Usuarios.insert_img(session["id"], filename) 
            session["img"] = filename
    if request.form.get('username'):
        new_name = request.form.get('username')
        Usuarios.new_name(session["id"], new_name)
        session["username"] = new_name
    return redirect("/profile")

@app.route("/request/", methods=["GET"])
def request_page():
    return render_template("new_book.html")

@app.route("/request/", methods=["POST"])
def request_send():
    title = request.form.get("title")
    author = request.form.get("author")
    isbn = request.form.get("isbn")
    year = request.form.get("year")
    reason = request.form.get("reason")
    data = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "reason": reason
    }
    Sugerencia.add_request(data)
    return redirect("/")

@app.route("/sugerencias/", methods=["GET"])
def sugerencias():
    sugerencias = Sugerencia.get_all()
    return render_template("sugerencias.html", sugerencias=sugerencias)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)