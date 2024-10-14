import pandas as pd
import psycopg2


df = pd.read_excel('books_data.xlsx')

conn = psycopg2.connect(
    dbname='books_db',   
    user='postgres',    
    password='mot de passe',  
    host='localhost',     
    port='5432'           
)


cursor = conn.cursor()

# Créer une commande d'insertion
insert_query = """
INSERT INTO books (titre, prix, disponibilite, rating) 
VALUES (%s, %s, %s, %s);
"""

# Insérer les données dans la table
# for index, row in df.iterrows():
#     cursor.execute(insert_query, (row['Titre'], row['Prix'], row['Disponibilité'], row['Rating']))

# Commit les changements
conn.commit()

# Fermer le curseur et la connexion
cursor.close()
conn.close()

print("Données insérées avec succès.")
