import sense_hat
import time

sh = sense_hat.SenseHat()

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

appPath = 'temperature'

mqtt_broker = "localhost"
mqtt_port = 1883

def onConnect(client, userData, retCode):
    print("Connected to broker, ")
    client.publish('temperature', '{"name":"sensehat", "desc":"Sensehat to MQTT bridge"}')

client = mqtt.Client(client_id = "sh2mqtt_bridge",
                    clean_session = True)

client.on_connect = onConnect
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()
while 1:
    time.sleep(1)
    temperature = sh.get_temperature()
    client.publish(appPath, temperature)
