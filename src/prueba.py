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
def get_book_info(isbn):
    print(isbn)
    response = requests.get(API_LINK + isbn)
    response.raise_for_status()
    data = response.json()
    volume_info = data["items"][0]["volumeInfo"]

    title = volume_info.get(TITLE_KEY)
    authors = volume_info.get(AUTHORS_KEY)
    published_date = volume_info.get(PUBLISHED_DATE_KEY)
    description = volume_info.get(DESCRIPTION_KEY)
    page_count = volume_info.get(PAGE_COUNT_KEY)
    key_words = ["fiction", "literary", "literature", "education"]
    categories = volume_info.get(CATEGORIES_KEY)
    new_categories = []
    if len(categories) < 1:
        for text in categories:
            new_categories.append(translate(text))
    else:
        new_categories.append(translate(categories[0]))
    image_links = volume_info.get(IMAGE_LINKS_KEY)

    book = {
        "isbn": isbn,
        "titulo": title,
        "autores": authors if authors else 'NA',
        "fecha_publicacion": published_date if published_date else 'NA',
        "paginas": page_count,
        "descripcion": description.replace("--Publisher's description.", "").replace("'", "\\'").replace('"', '\\"') if description else 'NA',
        "generos": new_categories,
        "imagen": image_links[THUMBNAIL_KEY] if image_links else 'NA'
    }
    return book

if __name__ == "__main__":
    isbn = input("Ingresa el ISBN de tu libro (sin guiones): ")
    print(get_book_info(isbn))