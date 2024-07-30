from flask import Flask, render_template, request, session
from models.libros import Libros
from models.generos import Generos
from models.autores import Autores
from models.insert import Insert
from prueba import get_book_info
app = Flask(__name__)

app.secret_key = b'Y\af1Xz\f15\xad|eQ\x72t \xca\x1a\x10K'

@app.route("/", methods=["GET", "POST"])
def index():
    books = Libros.get_all()
    return render_template("index.html",books=books,categories=categories)

@app.route("/search/", methods=["GET", "POST"])
def search():
    search = request.args.get("search")
    books = Libros.search(search)
    return render_template("search.html",books=books) 

@app.route("/categories", methods=["GET"])
def categories():
    books = Libros.get_all()
    categories = Generos.get_categories_list(Generos)
    category = "Libros destacados"
    return render_template("categories.html",category=category,books=books,categories=categories)

@app.route("/category/<category>", methods=["GET"])
def categorie(category):
    category_for_book = Generos.get_all(category)
    books = Libros.get_all_for_category(Libros, category_for_book)
    categories = Generos.get_categories_list(Generos)
    return render_template("categories.html",category=category,books=books,categories=categories,category_for_book=category_for_book)


@app.route("/book/<bookid>/", methods=["GET"])
def a(bookid):
    book = Libros.get_book(Libros, bookid)
    authors = Autores.get_all(bookid)
    categories = Generos.get_category(Generos, bookid)
    print(categories)
    return render_template("book.html", book=book, authors=authors, categories=categories)

responses = []

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        response = request.form.get("isbn")
        book = get_book_info(response)
        if book:
            response2 = Insert.insert_all(book)
            if response2 == False:
                return "ISBN INVALIDO / NO TIENE IMAGEN"
        else: return "ISBN INVALIDO"
    return render_template("insert.html")

@app.route("/", methods=["POST"])
def hello_world_post():
    return "Hello, World! POST"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
