import mysql.connector
import db_config

class Sql:
    """
    Manage the connection to SQL and creates
    all the tables in the database
    """
    def __init__(self):
        """
        Connection to SQL
        """
        self.connect()

    def connect(self):
        """
        Connection to SQL via db_config file
        """
        self.connection = mysql.connector.connect(
            host = db_config.HOST,
            user = db_config.USER,
            password = db_config.PASSWORD,
            port = db_config.PORT,
            auth_plugin = db_config.AUTH_PLUGIN,
            database = db_config.DATABASE,
            charset = db_config.CHARSET,
            collation = db_config.COLLATION
        )
        mycursor = self.connection.cursor()
        mycursor.execute(f'USE {db_config.DATABASE}')

    def dbinit(self):
        """
        Tables creation via the .sql file
        """
        mycursor = self.connection.cursor()
        # mycursor.execute(f'CREATE DATABASE {db_config.DATABASE} CHARACTER SET {db_config.CHARSET} COLLATE {db_config.COLLATION}')
        sql_file = open('script-db/create_db.sql')
        sql_as_string = sql_file.read().split(";")
        mycursor.execute('USE openfoodfacts4')
        for sql in sql_as_string:
            mycursor.execute(sql)
        self.connection.commit()
        mycursor.close()
