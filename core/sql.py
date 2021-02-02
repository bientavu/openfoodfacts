import mysql.connector
from core.openfoodfacts import products_lst

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
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('CREATE DATABASE IF NOT EXISTS openfoodfacts2')
        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read()
        self.mycursor.execute('USE openfoodfacts2')
        self.mycursor.execute(sql_as_string, multi=True)

    def insertdata(self):
        self.mycursor = self.mydb.cursor()
        sql = 'INSERT INTO Product (name_product, link) VALUES (%s, %s)'
        values = products_lst
        self.mycursor.executemany(sql, values)
        self.mydb.commit()

