from pprint import pprint
from core.database import Sql
from core.models import Category, Product
from core.openfoodfacts import ProductDownloader, ProductCleaner
from core.views import View
from core.controllers import Controller

# hello = WelcomeMenu()
# say_hello = hello.hello()

view = View()
product = Product

program_controller = Controller(view, product)
program_controller.run()

# create_database = Sql()
# create_database.dbinit()

# Category.objects.insert_categories()

# products = ProductDownloader()
# products_dict = products.get_products_info()

# cleaner = ProductCleaner()
# cleaned_products = cleaner.clean(products_dict)

# Product.objects.insert_product(cleaned_products)

# Product.objects.fetch_all_products()
