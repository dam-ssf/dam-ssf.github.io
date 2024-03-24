from pprint import pprint
from pypartpicker import Scraper

# search for a part using pypartpicker module
part = input("Enter a part to search for: ")
scraper = Scraper()
search = scraper.part_search(part, region="es")
for item in search:
    print("Fetching", item.url, "...")
    product = scraper.fetch_product(item.url)
    product = {
        "name": product.name,
        "price": product.price,
        "specs": product.specs
    }
    pprint(product)

