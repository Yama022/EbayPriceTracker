import sys
import os

# Ajout du chemin du répertoire 'src' au système path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(os.path.abspath(parent_dir))

from scraper import fetch_recent_price

# Liste des articles à rechercher
items = ["ETB Flammes Obsidiennes", "Display Faille Paradoxe", 'Display Flammes Obsidiennes', "Coffret Pikachu V", "Noctali V PSA10"]
for item in items:
    price, sale_date = fetch_recent_price(item)
    if price is None:
        print(f"Aucun article vendu récemment pour '{item}' sur eBay.fr.")
    else:
        print(f"Le dernier article '{item}' a été vendu sur eBay.fr pour €{price:.2f} le{sale_date}.")
