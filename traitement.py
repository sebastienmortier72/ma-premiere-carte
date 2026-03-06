import geopandas as gpd
from datetime import datetime
import os

try:
    # 1. Lecture du fichier source
    print("Lecture du fichier communes_test.geojson...")
    df = gpd.read_file('communes_test.geojson')

    # --- CORRECTION DU SYSTÈME DE COORDONNÉES ---
    # On force la conversion vers le WGS84 (EPSG:4326) utilisé par Leaflet
    print("Conversion des coordonnées vers WGS84...")
    df = df.to_crs(epsg=4326)
    # --------------------------------------------

    # 2. Ajout de l'heure du robot
    maintenant = datetime.now().strftime("%H:%M:%S")
    df['status_robot'] = f"Mis à jour à {maintenant}"
    print(f"Robot actif à {maintenant}")

    # 3. Sauvegarde du résultat final
    # On s'assure de sauvegarder en GeoJSON propre pour le web
    df.to_file('resultat.geojson', driver='GeoJSON')
    print("Fichier resultat.geojson créé avec succès en WGS84 !")

except Exception as e:
    print(f"Erreur pendant le traitement : {e}")
    exit(1)
