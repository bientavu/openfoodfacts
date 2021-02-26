from core.constants import CATEGORIES

class BaseManager:
    def __init__(self, connection):
        self.db = connection

class ProductManager(BaseManager):
    pass


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