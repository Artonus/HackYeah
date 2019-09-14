import paho.mqtt.client as mqtt
import sys

client = mqtt.Client() # client_id randomly generated, apparently

client.connect("test.mosquitto.org") #zamienic na IP

argNum = len(sys.argv)
n=0 #witamy na WDI

if argNum % 2 != 0:
    print("Odd number of parameters!")

while n < argNum:
    client.publish(sys.argv[n],sys.argv[n+1])
    n += 2