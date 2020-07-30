import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='46.17.173.183',
                                         database='u9465597_PLN ',
                                         user='u9465597_PLN1 ',
                                         password='password123')
    mySql_insert_query = """INSERT INTO data_sensor (Id, sensor_1, sensor_2) 
                           VALUES (10, 6459, 123 ) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


