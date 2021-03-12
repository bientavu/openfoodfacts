from core.constants import CATEGORIES
from core.managers import ProductManager, CategoryManager, SubstituteManager
from core.database import Sql

database = Sql()

class Product:

    objects = ProductManager(database)

    def __init__(self, name, store, nutriscore, link, category):
        self.id = None
        self.name = name
        self.score = store
        self.nutriscore = nutriscore
        self.link = link
        self.category = category


class Category:

    objects = CategoryManager(database)

    def __init__(self, category, products):
        self.id = None
        self.category = category
        self.products = products


class Substitute:

    objects = SubstituteManager(database)

    def __init__(self, id_product_to_substitute, id_product_substitute):
        self.id = None
        self.id_product_to_substitute = id_product_to_substitute
        self.id_product_substitute = id_product_substitute



