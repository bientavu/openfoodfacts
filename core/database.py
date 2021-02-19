import mysql.connector

class Sql:
    def __init__(self):
        self.connection()

    def connection(self):
        """
        Connection to SQL via localhost root user
        """
        self.mydb = mysql.connector.connect(option_files='db_configuration.conf')

    def dbinit(self):
        """
        Database creation + Tables creation via .sql file
        """
        mycursor = self.mydb.cursor()
        mycursor.execute('CREATE DATABASE IF NOT EXISTS openfoodfacts')
        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read()
        mycursor.execute('USE openfoodfacts')
        for result in mycursor.execute(sql_as_string, multi=True):
            pass
        self.mydb.commit()
        mycursor.close()
