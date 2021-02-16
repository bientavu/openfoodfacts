from core2.constants import CATEGORIES

class BaseManager:
    def __init__(self, mydb):
        self.mydb = mydb

class ProductManager(BaseManager):
    pass

class CategoryManager(BaseManager):
    def category_table_mapping(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE openfoodfacts3')
        for category in CATEGORIES:
            sql = "INSERT INTO Category (name_cat) VALUES ('{}');".format(category)
            self.mycursor.execute(sql)
            self.mydb.commit()


class SubstituteManager(BaseManager):
    pass