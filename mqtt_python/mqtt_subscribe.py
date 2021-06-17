from paho.mqtt import client as mqtt_client
import random

broker = 'm16.cloudmqtt.com'
port = 15372
topic = 'outTopic'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'dwvkqzpd'
password = 'uEzJFy5rb_Ra'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected to Mqtt Broker!')
        else:
            print('ailed to connect, return code %d\n', rc)
    
    #connecting to client id
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f'Received {msg.payload.decode()} from {msg.topic} topic')

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()


            
