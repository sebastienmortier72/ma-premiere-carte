import geopandas as gpd
import os

# 1. Charger ton fichier (Vérifie bien que le nom correspond à ton fichier monté sur GitHub)
nom_du_gros_fichier = 'parcellaire_drome.geojson'

print("Chargement du fichier source...")
df = gpd.read_file(nom_du_gros_fichier)

# 2. Créer le dossier qui va recevoir les petites communes
if not os.path.exists('communes'):
    os.makedirs('communes')
    print("Dossier 'communes' créé.")

# 3. On trouve le nom de la colonne qui contient le nom de la ville
# ATTENTION : Si dans ton fichier c'est 'NOM' ou 'city', change le mot 'nom_comm' ci-dessous
colonne_commune = 'nom_comm' 

villes = df[colonne_commune].unique()

# 4. On boucle pour créer un fichier par ville
for ville in villes:
    if ville is not None:
        df_ville = df[df[colonne_commune] == ville]
        # On nettoie le nom pour éviter les erreurs (ex: "Valence" -> "valence.geojson")
        nom_fich = str(ville).replace(" ", "_").replace("'", "_").lower()
        df_ville.to_file(f'communes/{nom_fich}.geojson', driver='GeoJSON')
        print(f"Export de : {ville}")

print("Opération terminée avec succès !")
