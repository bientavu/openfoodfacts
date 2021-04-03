from . import models
from .constants import CATEGORIES

class BaseManager:
    """
    Connects all the managers to SQL by using database.py
    """
    def __init__(self, connection):
        """
        Database connection
        """
        self.db = connection

class ProductManager(BaseManager):
    """
    Manage the products in the SQL database
    """
    def insert_product(self, products):
        """
        Inserts all the products into the SQL Product table
        """
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
        """
        Fetch all the products from the SQL Product table
        so that the controllers can call them
        """
        mycursor = self.db.connection.cursor()
        mycursor.execute("""
            SELECT Product.id, name_product, category_fk, store, nutriscore, link
            FROM Product
            INNER JOIN Category 
            ON Product.category_fk = Category.id
            WHERE Category.name_cat = %(category)s""",
            {"category": category.name_cat}
            )
        myresult = mycursor.fetchall()

        results = []

        for line in myresult:
            id = line[0]
            name_product = line[1]
            category_fk = line[2]
            store = line[3]
            nutriscore = line[4]
            link = line[5]
            results.append(models.Product(
                id=id,
                name=name_product,
                category=category_fk,
                store=store,
                nutriscore=nutriscore,
                link=link
                ))

        return results

    def fetch_selected_product(self, product):
        """
        Fetch the product selected by the use from the
        SQL Product table so that the controllers can call it
        """
        mycursor = self.db.connection.cursor()
        mycursor.execute("""
            SELECT Product.id, name_product, category_fk, store, nutriscore, link
            FROM Product
            WHERE Product.id = %(product)s""",
            {"product": product.id}
            )
        myresult = mycursor.fetchone()

        results = []

        results.append(models.Product(
            id=myresult[0],
            name=myresult[1],
            category=myresult[2],
            store=myresult[3],
            nutriscore=myresult[4],
            link=myresult[5]
            ))

        return results

    def fetch_better_product(self, category):
        """
        Fetch randomly one product from the SQL Product table
        that is better than the one selected by the user
        """
        mycursor = self.db.connection.cursor()
        mycursor.execute("""
            SELECT Product.id, name_product, category_fk, store, nutriscore, link
            FROM Product
            INNER JOIN Category
            ON Product.category_fk = Category.id
            WHERE Category.name_cat = %(category)s
            AND (Product.nutriscore = 'a' OR Product.nutriscore = 'b')
            ORDER BY RAND()
            LIMIT 1""",
            {"category": category.name_cat})
        myresult = mycursor.fetchone()

        results = []

        results.append(models.Product(
            id = myresult[0],
            name=myresult[1],
            category=myresult[2],
            store=myresult[3],
            nutriscore=myresult[4],
            link=myresult[5]
            ))

        return results
    
class CategoryManager(BaseManager):
    """
    Manage the categories in the SQL database
    """
    def insert_categories(self):
        """
        Inserts all the categories from the constant.py
        module into the SQL Category table
        """
        mycursor = self.db.connection.cursor()
        sql = "INSERT INTO Category (name_cat) VALUES (%(cat_name)s)"
        for category in CATEGORIES:
            mycursor.execute(sql, {'cat_name' : category})
        self.db.connection.commit()

    def fetch_all_categories(self):
        """
        Fetch all the categories from the SQL Category table
        so that the controllers can call them
        """
        mycursor = self.db.connection.cursor()
        mycursor.execute("SELECT name_cat FROM Category")
        myresult = mycursor.fetchall()

        results = []

        for line in myresult:
            cat_name = line[0]
            results.append(models.Category(name_cat=cat_name))

        return results

class SubstituteManager(BaseManager):
    """
    Manage the substitutes in the SQL database
    """
    def insert_substitute(self, selected_product, better_product):
        """
        Inserts substitutes into the SQL table
        when the user choose this option
        """
        mycursor = self.db.connection.cursor()
        mycursor.execute("""
        INSERT INTO Substitute (id_product_to_substitute, id_product_substitute)
        VALUES (%(id_product_to_substitute)s, %(id_product_substitute)s)
        """,
        {"id_product_to_substitute" : selected_product[0].id,
        "id_product_substitute" : better_product[0].id})

        self.db.connection.commit()

    def fetch_substitute_list(self):
        """
        Fetch all the substitutes from the SQL Substitute table
        so that the controllers can call them
        """
        mycursor = self.db.connection.cursor()
        mycursor.execute("""
            SELECT selected_product.id, selected_product.name_product,
            selected_product.store, selected_product.nutriscore,
            selected_product.link, selected_product.category_fk,
            better_product.id, better_product.name_product,
            better_product.store, better_product.nutriscore,
            better_product.link, better_product.category_fk 
            FROM Substitute
            JOIN Product AS selected_product ON Substitute.id_product_to_substitute = selected_product.id
            JOIN Product AS better_product ON Substitute.id_product_substitute = better_product.id
            """)
        myresult = mycursor.fetchall()

        results = []

        for result in myresult:
            results.append((models.Product(*result[:6]), models.Product(*result[6:])))

        return results
