import requests
from core.constants import CATEGORIES
from pprint import pprint

class Data:
    def __init__(self):
        self.products_lst = list()

    def get_information_product(self):
        """
        Grad the data from the Openfoodfact API
        """
        base_url = 'https://fr.openfoodfacts.org/'

        for category in CATEGORIES:
            categorie_url = f'{base_url}categorie/{category}.json'
            response = requests.request('GET', categorie_url).json()
            all_products = response.get('products')
            hundred_products = all_products[:100]

            for data in hundred_products:
                product = dict()
                product['product_name_fr'] = data.get('product_name_fr')
                product['url'] = data.get('url')
                product['nutriscore_grade'] = data.get('nutriscore_grade')
                product['stores'] = data.get('stores')
                self.products_lst.append(product)

        # pprint(products_lst)
        return self.products_lst

    def products_dict_to_query(self):
        """
        Creates a query that allows to add products informations
        into the SQL Product Table
        """
        sql_product_query = ''
        for product in self.products_lst:
            adding_values = [f'"{x}"' for x in product.values()]
            query = "INSERT INTO Product (%s) VALUES (%s);" % (
                ", ".join(product.keys()),
                ", ".join(adding_values),
                )
            
            sql_product_query += query

        pprint(sql_product_query)