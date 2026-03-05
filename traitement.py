import geopandas as gpd
from datetime import datetime

# 1. On lit ton fichier de test
df = gpd.read_file('communes_test.geojson')

# 2. On ajoute une preuve que le robot a travaillé
maintenant = datetime.now().strftime("%H:%M:%S")
df['status_robot'] = f"Traité avec succès à {maintenant}"

# 3. On enregistre le résultat que la carte va lire
df.to_file('resultat.geojson', driver='GeoJSON')

print(f"Le robot a terminé son job à {maintenant}")
