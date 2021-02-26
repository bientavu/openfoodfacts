from core.database import Sql
from core.models import Category, Product
from core.openfoodfacts import ProductCleaner

# create_database = Sql()
# create_database.dbinit()

# Category.objects.insert_category()
# Product.objects.get_products_info()


clean = ProductCleaner()
clean.store_clean()


# connection.category_mapping()