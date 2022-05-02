from classes.sport import Sport
from helper.mysqlconnector import connect
from mysql.connector import Error

football = Sport(1, "football")
query = '''
    INSERT INTO Sport(name) VALUES(%s) ;
'''

mysqlconnection = connect()
conn = mysqlconnection.cursor()

try:
    conn.execute(query, ["Football"])
    mysqlconnection.commit()
    print("Inserted")
except(Exception, Error) as e:
    print(e)

print('Welcome to SneakerWolf')
