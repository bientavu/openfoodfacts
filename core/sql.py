import mysql.connector
# from core.openfoodfacts import products_lst
from core.constants import CATEGORIES

class Sql:
    def __init__(self):
        self.connection()

    def connection(self):
        """
        Connection to SQL via localhost root user
        """
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azqsazqs282',
            auth_plugin = 'mysql_native_password'
        )

    def dbinit(self):
        """
        Database creation + Tables creation via .sql file
        """
        mycursor = self.mydb.cursor()
        mycursor.execute('CREATE DATABASE IF NOT EXISTS openfoodfacts4')
        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read()
        mycursor.execute('USE openfoodfacts4')
        for result in mycursor.execute(sql_as_string, multi=True):
            pass
        self.mydb.commit()
        mycursor.close()


class Category:
    def category_mapping(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE openfoodfacts3')
        for category in CATEGORIES:
            sql = "INSERT INTO Category (name_cat) VALUES ('{}');".format(category)
            self.mycursor.execute(sql)
            self.mydb.commit()
            # print(self.mycursor.rowcount, "record was inserted.")



    def product_mapping(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE openfoodfacts3')


        