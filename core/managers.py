from core.constants import CATEGORIES

class BaseManager:
    def __init__(self, connection):
        self.db = connection

class ProductManager(BaseManager):
    def insert_product(self, products):
        mycursor = self.db.connection.cursor()
        sql = """
        INSERT INTO Product (name_product, category_fk, store, nutriscore, link)
        VALUES (%(name_product)s, (SELECT id FROM Category WHERE name=%(name_cat)s), %(store)s, %(nutriscore)s, %(link)s)
        """
        for product in products:
            for product_name, name_cat, stores, nutriscore_grade, url in product.items():
                mycursor.execute(sql, {
                    'name_product' : product_name,
                    'name_cat' : name_cat,
                    'store' : stores,
                    'nutriscore' : nutriscore_grade,
                    'link' : url
                    })
        self.db.connection.commit()

class CategoryManager(BaseManager):
    def insert_category(self):
        mycursor = self.db.connection.cursor()
        # mycursor.execute('USE openfoodfacts')
        sql = "INSERT INTO Category (name_cat) VALUES (%(cat_name)s)"
        for category in CATEGORIES:
            mycursor.execute(sql, {'cat_name' : category})
        self.db.connection.commit()

class SubstituteManager(BaseManager):
    pass