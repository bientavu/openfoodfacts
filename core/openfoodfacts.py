import requests
from pprint import pprint
from .constants import CATEGORIES

class ProductDownloader:
    """
    Download all the informations of the products.
    Categories are setup in the module constant.py
    """
    def get_products_info(self):
        """
        Gets all the products informations and put in a list
        """
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
    """
    Cleans the list that has been downloaded by
    the method get_products_info
    """
    def remove_empty_values(self, product):
        """
        Removes all the empty values from the list
        """
        res = {key: val for key, val in product.items() if val}
        return res

    def clean(self, products):
        """
        Add all the cleaned products to a new list only if
        lenght is 5, name length under 100 and store name under 45
        """
        cleaned_products = []

        for product in products:
            product = self.remove_empty_values(product)
            if len(product) == 5 and len(product['product_name']) < 100 and len(product['stores']) < 45:
                cleaned_products.append(product)
                
        return cleaned_products