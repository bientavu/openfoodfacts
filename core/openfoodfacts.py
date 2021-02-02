import requests
from core.constants import CATEGORIES
from pprint import pprint

products_lst = list()

class Data:
    def __init__(self):
        pass

    def _get_information_product(self):
        """
        Grad the data from the Openfoodfact API
        """
        base_url = 'https://fr.openfoodfacts.org/'
        # product_name_fr = all_products.get('product_name_fr')

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
                products_lst.append(product)

        pprint(products_lst)

        return products_lst
