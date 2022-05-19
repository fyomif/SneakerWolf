import mysql.connector

def init():
    global cnx

    cnx = mysql.connector.connect(user='admin', password='password',
                                    host='127.0.0.1',
                                    database='wolfwind2')

    


    