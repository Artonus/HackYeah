import paho.mqtt.client as mqtt

def on_connectEvent(client, userdata, flags, rc):
        if rc == 0:
            print("Conn working")
            pass
        else:
            print("Conn not working")
            pass
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.        
        pass

def on_messageEvent(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    pass
    
# move type: move or freq
def sendCommand(self, moveType, value):
    self._client.wait(4)
    # obosolete:
    # message = "mosquitto_pub -h 192.168.0.1 -t {mov} -m {val}".format(fre = value, mov = moveType)        
    self._client.subscribe(moveType)
    self._client.publish(moveType, value)
    print("Command send: ", moveType, value)
    
    pass

conn = mqtt.Client("P1")
broker_address="mqtt.eclipse.org" #"192.168.0.1"
port = 1883

conn.on_connect = on_connectEvent
conn.on_message = on_messageEvent
conn.connect(broker_address, port, 60)

conn.loop_start()
conn.subscribe('move')
conn.publish('move', 'stop')
conn.subscribe('freq')
conn.publish('freq', 50)
conn.subscribe('move')
conn.publish('move', 'left')

conn.disconnect()
conn.loop_stop()