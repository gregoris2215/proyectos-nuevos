# scraper_noticias.py

import requests
from bs4 import BeautifulSoup

def obtener_noticias(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = soup.find_all('h2')
    titulares = [noticia.text for noticia in noticias]
    return titulares

def main():
    url = 'https://www.bbc.com/'
    titulares = obtener_noticias(url)
    for i, titular in enumerate(titulares, start=1):
        print(f"{i}. {titular}")

if __name__ == "__main__":
    main()
