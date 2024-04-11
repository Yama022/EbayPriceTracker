import sys
import os

# Ajout du chemin du répertoire 'src' au système path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(os.path.abspath(parent_dir))

from scraper import fetch_highest_price

# Définissez le nom de l'article à rechercher
item_name = "Display Pokémon Faille Paradoxe"

# Appelez la fonction pour récupérer le prix le plus élevé
# highest_price = fetch_highest_price(item_name)

items = ["Display Pokémon Faille Paradoxe", "Pokémon Stars Étincellantes", "ETB Pokémon Flammes Obsidiennes"]
for item in items:
    highest_price = fetch_highest_price(item)
    print(f"Le prix le plus élevé récemment pour '{item}' sur eBay.fr est de €{highest_price:.2f}")


# Affichez le résultat
print(f"Le prix le plus élevé récemment pour '{item_name}' sur eBay est de ${highest_price:.2f}")
