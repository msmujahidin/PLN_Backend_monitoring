import json
import paho.mqtt.client as mqtt
import schedule
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="umitransport.com",
  user="u9465597_PLN1",
  password="password123",
  database="u9465597_PLN"
)

username = "mqtt"
password = "mqtt"
topic = "pln"
broker_ip = ""

mycursor = mydb.cursor()

client = mqtt.Client()
client.username_pw_set(username, pasword)

def on_connect(client, userdata, flags, rc):
    print("Connected!", str(rc))
    client.subscribe(topic)

def lifo_insert(item, da_mem_list):
    okeh = da_mem_list.insert(0, item)  
    schedule.every().hour.do(okeh) 
    return da_mem_list[:24]

   
def on_message(client, userdata, msg):
    data = int(msg.payload)
    lifo_list = []
    lifo_list = lifo_insert(data, lifo_list)
   
    windows_size = 24

    i = 0
    moving_averages = []
        while i < len(lifo_list) - window_size + 1:
            this_window = lifo_list[i : i + window_size]
            window_average = sum(this_window) / window_size
            moving_averages.append(window_average)
            i += 1
    data_json = json.dumps(moving_averages)
    
    sql = ("INSERT INTO data_sensor "
       "(sensor_1) "
       "VALUES (%s)")
    
    field = mycursor.execute(sql, data_json)
    schedule.every().day.at("00:00").do(field)
    mydb.commit()    
    
    while True:
        schedule.run_pending() 
        time.sleep(1) 
        
    
    #print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
 
    
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker_ip, 1883)

client.loop_forever()
client.disconnect()

