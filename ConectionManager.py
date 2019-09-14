import paho.mqtt.client as mqtt

class Connection():

    _client = mqtt.Client("P1")

    @staticmethod
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

    @staticmethod
    def on_messageEvent(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        pass
    
    # move type: move or freq
    def sendCommand(self, moveType, value):        
        # obosolete:
        # message = "mosquitto_pub -h 192.168.0.1 -t {mov} -m {val}".format(fre = value, mov = moveType)        
        self._client.subscribe(moveType)
        self._client.publish(moveType, value)
        print("Command send: ", moveType, value)
        
        pass
    # Należy zawsze wykonać przed zamknięciem programu
    def disconnect(self):        
        self._client.disconnect()
        self._client.loop_stop()        
        pass

    def on_disconnect(client, userdata, rc):
        client.loop_stop()
        print("Disconected")
        pass

    def __init__(self):
        try:
            broker_address="mqtt.eclipse.org" #"192.168.0.1"
            port = 1883            
            self._client.on_connect = self.on_connectEvent
            self._client.on_message = self.on_messageEvent
            self._client.connect(broker_address, port, 60)
            
            self._client.loop_start()
            pass
        except Exception as ex:
            print(ex)
            pass             
        pass
    pass
