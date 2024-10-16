# 📚 Projet ETL : Scraping de Livres 🚀

## Description

Ce projet consiste en un pipeline ETL (Extract, Transform, Load) qui scrape les données de livres à partir d'un site web, les transforme et les charge dans une base de données PostgreSQL. Ce projet est une démonstration des compétences en scraping web, en manipulation de données et en gestion de base de données .

## Étapes du projet

1. **Extraction des Données (Scraping)** :
   - Utilisation de Python avec les bibliothèques `requests` et `BeautifulSoup` pour extraire les informations des livres à partir du site [Books to Scrape](http://books.toscrape.com).
   - Les données extraites comprennent :
     - Titre
     - Prix
     - Disponibilité
     - Rating

2. **Transformation des Données** :
   - Utilisation de la bibliothèque `pandas` pour nettoyer et transformer les données :
     - Conversion des prix en format numérique.
     - Mappage des évaluations (rating) en valeurs numériques.
     - Suppression des doublons.
   - Les données transformées sont ensuite enregistrées dans un fichier Excel nommé `books_data.xlsx`.

3. **Chargement des Données** :
   - Connexion à une base de données PostgreSQL à l'aide de la bibliothèque `psycopg2`.
   - Chargement des données transformées dans la table `books`.


## Prérequis

- Python 3.x
- Bibliothèques Python :
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl` (pour lire les fichiers Excel)
  - `psycopg2`
- PostgreSQL
