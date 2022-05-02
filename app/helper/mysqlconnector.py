import mysql.connector
import configparser
import os

from mysql.connector import Error

from dotenv import load_dotenv


def connect():
    try:
        # connect to database
        # reading the database parameters from the config object
        load_dotenv()
        conn = mysql.connector.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('username'),
            password=os.getenv('password'),
            port=os.getenv('port')
        )
        return conn
    except(Exception, Error) as error:
        print(error)
