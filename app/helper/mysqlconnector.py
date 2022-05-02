import mysql.connector
from mysql.connector import Error


def connect():
    try:
        # connect to database
        # reading the database parameters from the config object
        conn = mysql.connector.connect(
            host='localhost',
            database='sneakerwolf',
            user='admin',
            password='password',
            port='3306'
        )

        return conn
    except(Exception, Error) as error:
        print(error)
