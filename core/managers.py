from core.constants import CATEGORIES

class BaseManager:
    def __init__(self, mydb):
        self.mydb = mydb

class ProductManager(BaseManager):
    pass

class CategoryManager(BaseManager):
    def category_table_mapping(self):
        mycursor = self.mydb.cursor()
        mycursor.execute('USE openfoodfacts')
        for category in CATEGORIES:
            mycursor.execute("INSERT INTO Category (name_cat) VALUES ('%s')" % category)
            self.mydb.commit()


class SubstituteManager(BaseManager):
    pass