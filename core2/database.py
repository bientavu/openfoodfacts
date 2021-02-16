import mysql.connector

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
