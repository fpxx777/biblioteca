import requests
import json

API_LINK = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
ISBN_KEY = "isbn"
TITLE_KEY = "title"
AUTHORS_KEY = "authors"
PUBLISHED_DATE_KEY = "publishedDate"
DESCRIPTION_KEY = "description"
PAGE_COUNT_KEY = "pageCount"
CATEGORIES_KEY = "categories"
IMAGE_LINKS_KEY = "imageLinks"
SMALL_THUMBNAIL_KEY = "smallThumbnail"

def get_book_info(isbn):
    response = requests.get(API_LINK + isbn)
    response.raise_for_status()
    data = response.json()
    volume_info = data["items"][0]["volumeInfo"]

    title = volume_info.get(TITLE_KEY)
    authors = volume_info.get(AUTHORS_KEY)
    published_date = volume_info.get(PUBLISHED_DATE_KEY)
    description = volume_info.get(DESCRIPTION_KEY)
    page_count = volume_info.get(PAGE_COUNT_KEY)
    categories = volume_info.get(CATEGORIES_KEY)
    image_links = volume_info.get(IMAGE_LINKS_KEY)

    print(f"Título: {title}")
    print(f"Autores: {', '.join(authors) if authors else 'NA'}")
    print(f"Fecha de publicación: {published_date if published_date else 'NA'}")
    print(f"Descripción: {description if description else 'NA'}")
    print(f"Páginas: {page_count}")
    print(f"Géneros: {', '.join(categories) if categories else 'NA'}")
    print(f"Imagen: {image_links[SMALL_THUMBNAIL_KEY] if image_links else 'NA'}")

if __name__ == "__main__":
    isbn = input("Ingresa el ISBN de tu libro (sin guiones): ")
    get_book_info(isbn)