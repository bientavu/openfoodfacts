from pprint import pprint
from core.database import Sql
from core.models import Category, Product
from core.openfoodfacts import ProductDownloader, ProductCleaner

# create_database = Sql()
# create_database.dbinit()

# Category.objects.insert_category()
# Product.objects.get_products_info()

products = ProductDownloader()
products_dict = products.get_products_info()

cleaner = ProductCleaner()
cleaned_products = cleaner.clean(products_dict)

Product.objects.insert_product(cleaned_products)

# pprint(cleaned_products)


# connection.category_mapping()