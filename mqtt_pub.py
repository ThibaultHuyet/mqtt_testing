import sense_hat
import time

sense = sense_hat.SenseHat()

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

appPath = 'temperature'

mqtt_broker = "localhost"
mqtt_port = 1883

def onConnect(client, userData, retCode):
    print("Connected to broker, ")

client = mqtt.Client(client_id = "rpi2comp",
                    clean_session = True)

client.on_connect = onConnect
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()

while 1:
    temperature = sense.get_temperature()
    client.publish(appPath, temperature)
    time.sleep(1)