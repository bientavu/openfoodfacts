from pprint import pprint
from core.database import Sql
from core.models import Category, Product
from core.openfoodfacts import ProductDownloader, ProductCleaner
from core.program import WelcomeMenu

# hello = WelcomeMenu()
# say_hello = hello.Hello()

# create_database = Sql()
# create_database.dbinit()

# Category.objects.insert_category()

products = ProductDownloader()
products_dict = products.get_products_info()

cleaner = ProductCleaner()
cleaned_products = cleaner.clean(products_dict)

Product.objects.insert_product(cleaned_products)