import requests
import json


#"autores": ', '.join(authors) if authors else 'NA',
def translate(text):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": "en|es"
    }
    try:
        response = requests.get(url, params=params)
        translation = response.json()["responseData"]["translatedText"]
        return translation
    except requests.exceptions.RequestException as e:
        return None


API_LINK = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
ISBN_KEY = "isbn"
TITLE_KEY = "title"
AUTHORS_KEY = "authors"
PUBLISHED_DATE_KEY = "publishedDate"
DESCRIPTION_KEY = "description"
PAGE_COUNT_KEY = "pageCount"
CATEGORIES_KEY = "categories"
IMAGE_LINKS_KEY = "imageLinks"
THUMBNAIL_KEY = "thumbnail"
def get_book_info(isbn, info_faltante = {}):
    print(isbn)
    response = requests.get(API_LINK + isbn)
    response.raise_for_status()
    data = response.json()
    volume_info = data["items"][0]["volumeInfo"]

    errors = []
    title = volume_info.get(TITLE_KEY)
    authors = volume_info.get(AUTHORS_KEY)
    published_date = volume_info.get(PUBLISHED_DATE_KEY)
    description = volume_info.get(DESCRIPTION_KEY)
    page_count = volume_info.get(PAGE_COUNT_KEY)
    key_words = [
    "fiction", 
    "literary", 
    "literature", 
    "education", 
    "mystery", 
    "fantasy", 
    "science fiction", 
    "romance", 
    "thriller", 
    "horror", 
    "historical", 
    "biography", 
    "autobiography", 
    "poetry", 
    "drama", 
    "non-fiction", 
    "self-help", 
    "children's", 
    "young adult", 
    "dystopian"
]
    categories = volume_info.get(CATEGORIES_KEY)
    new_categories = []
    if categories and len(categories) > 0:
        for text in key_words:
            for cat in categories:
                if text in cat.lower(): 
                    new_categories.append(translate(text))
        if len(new_categories) == 0:
            new_categories.append(translate(categories[0]))    
    else:
        errors.append("generos")
    image_links = volume_info.get(IMAGE_LINKS_KEY)
    if info_faltante == {}:
        book = {
            "isbn": isbn,
            "titulo": title,
            "autores": authors if authors else errors.append("autores"),
            "fecha_publicacion": published_date if published_date else errors.append("fecha_publicacion"),
            "paginas": page_count,
            "descripcion": description.replace("--Publisher's description.", "").replace("'", "\\'").replace('"', '\\"') if description else errors.append("descripcion"),
            "generos": new_categories,
            "imagen": image_links[THUMBNAIL_KEY] if image_links else errors.append("img")
        }
    else:
        book = {
            "isbn": isbn,
            "titulo": title,
            "autores": authors if authors else info_faltante["autores"],
            "fecha_publicacion": published_date if published_date else info_faltante["fecha_publicacion"],
            "paginas": page_count,
            "descripcion": description.replace("--Publisher's description.", "").replace("'", "\\'").replace('"', '\\"') if description else info_faltante["descripcion"],
            "generos": new_categories if new_categories != [] else info_faltante["generos"],
            "imagen": image_links[THUMBNAIL_KEY] if image_links else info_faltante["img"]
        }
    return errors, book

if __name__ == "__main__":
    isbn = input("Ingresa el ISBN de tu libro (sin guiones):")
    print(get_book_info(isbn))