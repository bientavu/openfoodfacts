from core.constants import CATEGORIES

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
            for key, value in product.items():
                mycursor.execute(sql, {
                    'name_product' : product['product_name'],
                    'name_cat' : product['main_category'],
                    'store' : product['stores'],
                    'nutriscore' : product['nutriscore_grade'],
                    'link' : product['url']
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