import requests
from pprint import pprint
from core.constants import CATEGORIES

class BaseManager:
    def __init__(self, connection):
        self.db = connection

class ProductManager(BaseManager):
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
        
        pprint(products)


    def insert_product(self):
        pass

class ProductCleaner():
    def store_clean(self):
        pprint(products)

class CategoryManager(BaseManager):
    def insert_category(self):
        mycursor = self.db.connection.cursor()
        # mycursor.execute('USE openfoodfacts')
        sql = "INSERT INTO Category (name_cat) VALUES (%(cat_name)s)"
        for category in CATEGORIES:
            mycursor.execute(sql, {'cat_name' : category})
        self.db.connection.commit()

class SubstituteManager(BaseManager):
    pass