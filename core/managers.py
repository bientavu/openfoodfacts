from . import models
from .constants import CATEGORIES
from pprint import pprint

class BaseManager:
    def __init__(self, connection):
        self.db = connection

class ProductManager(BaseManager):
    def insert_product(self, products):
        mycursor = self.db.connection.cursor()
        sql = """
        INSERT INTO Product (name_product, category_fk, store, nutriscore, link)
        VALUES (%(name_product)s, (SELECT id FROM Category WHERE name_cat=%(name_cat)s), %(store)s, %(nutriscore)s, %(link)s)
        """
        for product in products:
            mycursor.execute(sql, {
                'name_product' : product['product_name'],
                'name_cat' : product['main_category'],
                'store' : product['stores'],
                'nutriscore' : product['nutriscore_grade'],
                'link' : product['url']
                })
        self.db.connection.commit()

    def fetch_all_products(self, category):
        # pprint(category)
        mycursor = self.db.connection.cursor()
        mycursor.execute("""
            SELECT name_product, category_fk, store, nutriscore, link
            FROM Product
            INNER JOIN Category 
            ON Product.category_fk = Category.id
            WHERE Category.name_cat = %(category)s""",
            {"category": category.name_cat}
            )
        myresult = mycursor.fetchall()

        results = []

        for line in myresult:
            name_product = line[0]
            category_fk = line[1]
            store = line[2]
            nutriscore = line[3]
            link = line[4]
            results.append(models.Product(
                name=name_product,
                category=category_fk,
                store=store,
                nutriscore=nutriscore,
                link=link
                ))

        return results
    
class CategoryManager(BaseManager):
    def insert_categories(self):
        mycursor = self.db.connection.cursor()
        # mycursor.execute('USE openfoodfacts')
        sql = "INSERT INTO Category (name_cat) VALUES (%(cat_name)s)"
        for category in CATEGORIES:
            mycursor.execute(sql, {'cat_name' : category})
        self.db.connection.commit()

    def fetch_all_categories(self):
        mycursor = self.db.connection.cursor()
        mycursor.execute("SELECT name_cat FROM Category")
        myresult = mycursor.fetchall()

        results = []

        for line in myresult:
            cat_name = line[0]
            results.append(models.Category(name_cat=cat_name))

        return results

class SubstituteManager(BaseManager):
    pass