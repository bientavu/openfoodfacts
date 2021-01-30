import mysql.connector

class Sql:
    def __init__(self):
        self.connection()

    def connection(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azqsazqs282',
            auth_plugin = 'mysql_native_password'
        )

    def dbinit(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('CREATE DATABASE IF NOT EXISTS openfoodfacts2')
        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read()
        self.mycursor.execute('USE openfoodfacts2')
        self.mycursor.execute(sql_as_string, multi=True)

