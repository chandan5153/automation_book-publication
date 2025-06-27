# get_all_chapters.py
import requests
from bs4 import BeautifulSoup

def fetch_chapter_links(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    base_url = "https://en.wikisource.org"
    chapter_links = []

    for li in soup.select("div#mw-content-text ul li a"):
        href = li.get("href", "")
        if "/The_Gates_of_Morning/" in href:
            full_url = base_url + href
            chapter_links.append(full_url)

    return chapter_links
