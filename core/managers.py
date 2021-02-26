from core.constants import CATEGORIES

class BaseManager:
    def __init__(self, connection):
        self.mydb = connection

class ProductManager(BaseManager):
    pass

class CategoryManager(BaseManager):
    def insert_category(self):
        mycursor = self.mydb.cursor()
        mycursor.execute('USE openfoodfacts')
        for category in CATEGORIES:
            mycursor.execute("INSERT INTO Category (name_cat) VALUES ('%s')" % category)
        self.mydb.commit()

class SubstituteManager(BaseManager):
    pass