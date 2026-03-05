import geopandas as gpd
from datetime import datetime
import os

try:
    # 1. Lecture du fichier (vérifie bien que le nom est identique sur ton GitHub)
    print("Lecture du fichier communes_test.geojson...")
    df = gpd.read_file('communes_test.geojson')

    # 2. Ajout de l'heure du robot
    maintenant = datetime.now().strftime("%H:%M:%S")
    df['status_robot'] = f"Mis à jour à {maintenant}"
    print(f"Robot actif à {maintenant}")

    # 3. Sauvegarde du résultat final
    df.to_file('resultat.geojson', driver='GeoJSON')
    print("Fichier resultat.geojson créé avec succès !")

except Exception as e:
    print(f"Erreur pendant le traitement : {e}")
    exit(1)
