import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

broker = "192.168.0.3"
port = 1883
path = "temperature"

def on_message(client, userdata, message):
    temperature = float(message.payload)
    temperature = round(temperature, 2)
    print(str(message.topic) + ": {0}".format(temperature))

client = mqtt.Client(client_id = "sh2mqtt_bridge")
client.on_message = on_message

subscribe.callback(on_message, path, hostname = broker)
