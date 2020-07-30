import mysql.connector

mydb = mysql.connector.connect(
  host="umitransport.com",
  user="u9465597_PLN1",
  password="password123",
  database="u9465597_PLN"
)

print("Berhasil Connect")
mycursor = mydb.cursor()
print("okeh")

sql = ("INSERT INTO data_sensor "
       "(sensor_1, sensor_2) "
       "VALUES (%s, %s)")


val = ("100", "40")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

