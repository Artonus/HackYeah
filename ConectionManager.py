import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqtt

# The callback for when the client receives a CONNACK response from the server.
class Connection():
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        
    pass

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def __init__(self):
        broker_address="192.168.0.1"
        port = 1883
        self._topic = "mosquitto_pub"
        self._client = mqtt.Client(self._topic)
        self._client.on_connect = on_connect
        self._client.on_message = on_message
        self._client.connect(broker_address, port, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self._client.loop_forever()        
        pass
    # move type: move or freq
    def sendCommand(self, moveType, value):
        #obosolete
        #message = "mosquitto_pub -h 192.168.0.1 -t {mov} -m {val}".format(fre = value, mov = moveType)
        self._client.subscribe(moveType)
        self._client.publish(moveType, value)
        
        pass
    def disconnect(self):
        self._client.disconnect()
        pass
