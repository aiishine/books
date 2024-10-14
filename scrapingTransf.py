import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_books(url):
    #  HTTP pour récupérer le contenu
    response = requests.get(url)
    books_data = []


    if response.status_code == 200:
     
        soup = BeautifulSoup(response.text, 'lxml')

       
        books = soup.find_all('article', class_='product_pod')

        # Extraire les informations de chaque livre
        for book in books:
            title = book.h3.a['title'] 
            price = book.find('p', class_='price_color').text  
            availability = book.find('p', class_='instock availability').text.strip()  
            rating = book.p['class'][1]  

            # Ajouter les données dans la liste
            books_data.append({
                'Titre': title,
                'Prix': price,
                'Disponibilité': availability,
                'Rating': rating
            })

    return books_data

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Liste pour stocker les données des livres
all_books = []

for page_nbr in range(1, 7): 
    url = base_url.format(page_nbr)
    print(f"Scraping page {page_nbr}...")

    # Scraper les livres de la page actuelle
    books = scrape_books(url)

    if not books:  # Si aucune donnée n'est retournée, arrêter la boucle
        break

    all_books.extend(books)


df = pd.DataFrame(all_books)

# Transformations

df['Prix'] = df['Prix'].str.replace('£', '').str.replace('Â', '').str.replace(',', '.').astype(float) 

df['Rating'] = df['Rating'].map({
    'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
}) 

df.drop_duplicates(inplace=True)

print(df.head())

df.to_excel('books_data.xlsx', index=False)

print("Enregistrement avec succès")
