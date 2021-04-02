from core.database import Sql
from core.models import Category, Product
from core.openfoodfacts import ProductDownloader, ProductCleaner

def main():
    """
    Tables creation + products informations insertion
    """
    create_database = Sql()
    create_database.dbinit()

    Category.objects.insert_categories()

    products = ProductDownloader()
    products_dict = products.get_products_info()

    cleaner = ProductCleaner()
    cleaned_products = cleaner.clean(products_dict)

    Product.objects.insert_product(cleaned_products)

if __name__ == "__main__":
    main()