from flask import Flask, render_template

app = Flask(__name__)


books = [
    {
        "isbn": 9780307743671,
        "titulo": "'Salem's Lot",
        "autores": "Stephen King",
        "fecha de publicacion": "2011-12-27",
        "paginas": 674,
        "descripcion": "#1 BESTSELLER • Ben Mears has returned to Jerusalem’s Lot in hopes that exploring the history of the Marsten House, an old mansion long the subject of rumor and speculation, will help him cast out his personal devils and provide inspiration for his new book. But when two young boys venture into the woods, and only one returns alive, Mears begins to realize that something sinister is at work. In fact, his hometown is under siege from forces of darkness far beyond his imagination. And only he, with a small group of allies, can hope to contain the evil that is growing within the borders of this small New England town. With this, his second novel, Stephen King established himself as an indisputable master of American horror, able to transform the old conceits of the genre into something fresh and all the more frightening for taking place in a familiar, idyllic locale.",
        "generos": "Fiction",
        "imagen": "http://books.google.com/books/content?id=6OxSHEbM1isC&printsec=frontcover&img=1&zoom=5&source=gbs_api",
    },
    {
        "isbn": 9780307743671,
        "titulo": "'Salem's Lot",
        "autores": "Stephen King",
        "fecha de publicacion": "2011-12-27",
        "paginas": 674,
        "descripcion": "#1 BESTSELLER • Ben Mears has returned to Jerusalem’s Lot in hopes that exploring the history of the Marsten House, an old mansion long the subject of rumor and speculation, will help him cast out his personal devils and provide inspiration for his new book. But when two young boys venture into the woods, and only one returns alive, Mears begins to realize that something sinister is at work. In fact, his hometown is under siege from forces of darkness far beyond his imagination. And only he, with a small group of allies, can hope to contain the evil that is growing within the borders of this small New England town. With this, his second novel, Stephen King established himself as an indisputable master of American horror, able to transform the old conceits of the genre into something fresh and all the more frightening for taking place in a familiar, idyllic locale.",
        "generos": "Fiction",
        "imagen": "http://books.google.com/books/content?id=6OxSHEbM1isC&printsec=frontcover&img=1&zoom=5&source=gbs_api",
    },
    {
        "isbn": 9780307743671,
        "titulo": "'Salem's Lot",
        "autores": "Stephen King",
        "fecha de publicacion": "2011-12-27",
        "paginas": 674,
        "descripcion": "#1 BESTSELLER • Ben Mears has returned to Jerusalem’s Lot in hopes that exploring the history of the Marsten House, an old mansion long the subject of rumor and speculation, will help him cast out his personal devils and provide inspiration for his new book. But when two young boys venture into the woods, and only one returns alive, Mears begins to realize that something sinister is at work. In fact, his hometown is under siege from forces of darkness far beyond his imagination. And only he, with a small group of allies, can hope to contain the evil that is growing within the borders of this small New England town. With this, his second novel, Stephen King established himself as an indisputable master of American horror, able to transform the old conceits of the genre into something fresh and all the more frightening for taking place in a familiar, idyllic locale.",
        "generos": "Fictio",
        "imagen": "http://books.google.com/books/content?id=6OxSHEbM1isC&printsec=frontcover&img=1&zoom=5&source=gbs_api",
    }
]


@app.route("/", methods=["GET"])
def index():
    categoria = "Libros destacados"
    return render_template("index.html", categoria=categoria, books=books)


@app.route("/category/<categoria>", methods=["GET"])
def categorie(categoria):
    return render_template("index.html", categoria=categoria)


@app.route("/book/<bookid>/", methods=["GET"])
def a(bookid):
    return render_template("book.html")


@app.route("/", methods=["POST"])
def hello_world_post():
    return "Hello, World! POST"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
