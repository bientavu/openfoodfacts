import requests
from pprint import pprint
from core.constants import CATEGORIES

class ProductDownloader():
    def get_products_info(self):
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        number_of_pages = 2
        page_size = 100
        
        products = []

        for category in CATEGORIES:
            searched_category = category
        
            for page_number in range(1, number_of_pages+1):
                params = {
                    "action": "process",
                    "sort_by": "unique_scans_n", # popularité
                    "page_size": page_size,
                    "page": page_number, 
                    "fields": "product_name,categories,stores,nutriscore_grade,url",
                    "json": True,
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": searched_category
                    }
            
                response = requests.get(url, params=params)
                products.extend(response.json()["products"])

        return products


class ProductCleaner():
    def store_clean(self, products):
        pprint(products)