import paho.mqtt.publish as publish
import time

print("sending 0")
publish.single("ledstatus", "0", hostname="localhost")
time.sleep(0)
print("sending 1")
publish.single("ledstatus", "1", hostname="localhost")
