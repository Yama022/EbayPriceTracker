import requests
from bs4 import BeautifulSoup

def fetch_highest_price(search_query):
    search_query = '+'.join(search_query.split())
    # Mise à jour de l'URL pour utiliser eBay France et les prix en euros
    url = f"https://www.ebay.fr/sch/i.html?_nkw={search_query}&_sop=16&LH_Complete=1&LH_Sold=1&_ipg=200&LH_PrefLoc=2"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    highest_price = 0
    listings = soup.find_all('span', class_='s-item__price')
    for price in listings:
        price_text = price.text.replace('EUR', '').replace(',', '.').strip()
        try:
            price_value = float(price_text)
            if price_value > highest_price:
                highest_price = price_value
        except ValueError:
            continue

    return highest_price
