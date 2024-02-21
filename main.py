"""
Proyecto scrap-chelas
njofredev
Web scraping de cervezas artesanales de producción chilena
    - Uso de python
    - Uso de BeautifulSoup4
"""
# Se importa BeautifulSoup, Requests y CSV
from bs4 import BeautifulSoup
import requests
import csv

pagina_cervezas_del_sur = requests.get('https://cervezasdelsur.cl/pages/search-results-page?collection=marcas')
soup = BeautifulSoup(pagina_cervezas_del_sur.text, 'html.parser')

print(soup.prettify(soup.get_text()))


