from .managers import ProductManager, CategoryManager, SubstituteManager
from .database import Sql

database = Sql()

class Product:
    """
    Reprensents a food product with his name, nutriscore,
    category, where we can buy it and a openfoodfacts link
    """
    objects = ProductManager(database)

    def __init__(self, id, name, store, nutriscore, link, category):
        """
        Initialization of the product
        """
        self.id = id
        self.name = name
        self.store = store
        self.nutriscore = nutriscore
        self.link = link
        self.category = category


class Category:
    """
    Reprensents a category where multiples products are into
    """
    objects = CategoryManager(database)

    def __init__(self, name_cat):
        """
        Initialization of the category
        """
        self.id = None
        self.name_cat = name_cat


class Substitute:
    """
    Reprensents a product to substitute with his substitute
    """
    objects = SubstituteManager(database)

    def __init__(self, id_product_to_substitute, id_product_substitute):
        """
        Initialization of the products :
        (Product to substitute and Product substitute)
        """
        self.id = None
        self.id_product_to_substitute = id_product_to_substitute
        self.id_product_substitute = id_product_substitute



