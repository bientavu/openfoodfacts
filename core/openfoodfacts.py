import requests
from pprint import pprint
from core.constants import CATEGORIES

class ProductDownloader:

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
                    "fields": "product_name,stores,nutriscore_grade,url",
                    "json": True,
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": searched_category
                    }
            
                response = requests.get(url, params=params)
                products_data = response.json()["products"]
                for dictionary in products_data:
                    dictionary["main_category"] = category
                
                products.extend(products_data)

        return products


class ProductCleaner:
    def is_valid(self):
        pass

    def remove_empty_values(self, product):
        res = {key: val for key, val in product.items() if val}
        return res

    def clean(self, products):
        cleaned_products = []

        for product in products:
            product = self.remove_empty_values(product) # product est passé en argument de store_clean()
            if len(product) == 5 and len(product['product_name']) < 100 and len(product['stores']) < 45:
                cleaned_products.append(product) # le produit n'est ajouté que s'il est valide et après avoir été nettoyé
                
        return cleaned_products