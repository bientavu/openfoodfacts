import mysql.connector

class Sql:
    def connection(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azqsazqs282'
        )

    def dbinit(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('CREATE DATABASE openfoodfacts2')

        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read()
        self.mycursor.execute(sql_as_string)

