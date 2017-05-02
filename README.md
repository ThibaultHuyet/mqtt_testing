This is the very basic practice I started off doing to learn mqtt using Python.

# mqtt_basic.py
mqtt_basic.py is a very simple program that publishes a 0 and a 1 to a broker. This program was taken from some code I found online and it was intended to turn and LED on or off. I did not add the LED side and just wanted to see if I could get any kind of message sent.

#mqttSub.py
This was my first attempt at sending some sort of real values to a broker. The idea was just to receive messages from a raspberry pi with a sensehat. I perfomred some minor formating on the message to see what I could do with it.

#mqtt_pub.py
The publish code is run on the raspberry pi that has a Sensehat attached. I modified a lot of this code from sources I found online. I used a wide variaty and modified the entire code such that it isn really recognizable anymore. Sends a temperature value to any who subscribe to it.