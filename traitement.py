import geopandas as gpd
import os

# 1. Lecture du fichier Parquet (c'est très rapide !)
# Assure-toi que le nom du fichier sur GitHub est exactement celui-là
nom_fichier = 'parcellaire.parquet'

print("Chargement du Parquet...")
df = gpd.read_parquet(nom_fichier)

# 2. Création du dossier communes
if not os.path.exists('communes'):
    os.makedirs('communes')

# 3. On découpe (vérifie bien que le nom de ta colonne est 'nom_comm')
colonne_ville = 'nom_comm' 

villes = df[colonne_ville].unique()

for ville in villes:
    if ville is not None:
        df_ville = df[df[colonne_ville] == ville]
        # Nettoyage du nom de fichier
        nom_fich = str(ville).replace(" ", "_").replace("'", "_").lower()
        # On enregistre en GEOJSON (car c'est ce que la carte Web sait lire facilement)
        df_ville.to_file(f'communes/{nom_fich}.geojson', driver='GeoJSON')
        print(f"Exporté : {ville}")

print("Terminé !")
