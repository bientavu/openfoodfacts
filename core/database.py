import mysql.connector

class Sql:
    def __init__(self):
        self.connect()

    def connect(self):
        """
        Connection to SQL via localhost root user
        """
        self.connection = mysql.connector.connect(option_files='db_configuration.conf')
        mycursor = self.connection.cursor()
        mycursor.execute('USE openfoodfacts2')

    def dbinit(self):
        """
        Database creation + Tables creation via .sql file
        """
        mycursor = self.connection.cursor()
        mycursor.execute('CREATE DATABASE IF NOT EXISTS openfoodfacts2')
        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read()
        mycursor.execute('USE openfoodfacts2')
        for result in mycursor.execute(sql_as_string, multi=True):
            pass
        self.connection.commit()
        mycursor.close()
